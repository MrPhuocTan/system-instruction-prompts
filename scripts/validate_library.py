#!/usr/bin/env python3
"""Deterministic Architecture & Inventory Validator for the System Instruction Library.

Compatible with both standalone CLI execution and pytest:
  - python3 scripts/validate_library.py
  - pytest scripts/validate_library.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Sequence, Set, Tuple
from urllib.parse import unquote

LIBRARY_ROOT_DEFAULT = Path(__file__).resolve().parent.parent

ROOT_FILES: Tuple[str, ...] = (
    "README.md",
    "LIBRARY_INDEX.md",
    "VERSION.md",
    "CHANGELOG.md",
    "skills.json",
)

GLOBAL_CONSTITUTION_FILES: Tuple[str, ...] = (
    "GLOBAL_SYSTEM_PROMPT.md",
    "AGENT_GOVERNANCE.md",
    "TASK_COMPLEXITY_ROUTER.md",
    "COGNITIVE_EXECUTION.md",
    "INDEPENDENT_VERIFICATION.md",
    "SECURITY_AND_PRIVACY.md",
    "TOOL_USAGE_AND_LIMITATIONS.md",
    "HUMAN_APPROVAL_POLICY.md",
)

ORCHESTRATION_FILES: Tuple[str, ...] = (
    "ORCHESTRATION_SYSTEM_PROMPT.md",
    "AUTONOMOUS_ORCHESTRATION.md",
    "PROJECT_INITIALIZATION.md",
    "PROJECT_CONTEXT_MANAGEMENT.md",
    "PERSISTENT_PM_SA.md",
    "DYNAMIC_AGENT_ALLOCATION.md",
    "SUBAGENT_CREATION.md",
    "WORKSTREAM_MANAGEMENT.md",
    "AGENT_COMMUNICATION.md",
    "FILE_OWNERSHIP_AND_LOCKING.md",
    "CONTRACT_AND_HANDOFF.md",
    "REVIEW_AND_SIGNOFF.md",
    "PROGRESS_REPORTING.md",
)

CANONICAL_FILE_COUNT = 356

AUTONOMOUS_13_PHASES: Tuple[str, ...] = (
    "project initialization",
    "domain discovery",
    "domain mapping",
    "role discovery",
    "role research",
    "competency modeling",
    "boundary modeling",
    "skill engineering",
    "prompt generation",
    "quality review",
    "integration",
    "coverage auditing",
    "incremental continuation",
)

CORE_ROLES: Tuple[str, ...] = (
    "PROJECT_MANAGER",
    "SYSTEM_ARCHITECT",
    "DOMAIN_LEAD",
    "QUALITY_REVIEWER",
)

DOMAIN_ROLES: Dict[str, Tuple[str, ...]] = {
    "IT_SOFTWARE": (
        "SOFTWARE_ARCHITECT",
        "BACKEND_ENGINEER",
        "FRONTEND_ENGINEER",
        "FULLSTACK_ENGINEER",
        "DEVOPS_ENGINEER",
        "PLATFORM_ENGINEER",
        "DATABASE_ENGINEER",
        "QA_ENGINEER",
        "AUTOMATION_QA",
        "PERFORMANCE_ENGINEER",
        "SITE_RELIABILITY_ENGINEER",
    ),
    "CYBERSECURITY": (
        "SECURITY_ARCHITECT",
        "APPLICATION_SECURITY",
        "PENETRATION_TESTER",
        "RED_TEAM_OPERATOR",
        "BLUE_TEAM_SOC",
        "THREAT_INTELLIGENCE",
        "DIGITAL_FORENSICS",
        "INCIDENT_RESPONSE",
        "CLOUD_SECURITY",
        "NETWORK_SECURITY",
        "IAM_SPECIALIST",
        "SECURITY_GRC",
        "PRIVACY_SPECIALIST",
    ),
    "AI_MACHINE_LEARNING": (
        "AI_ARCHITECT",
        "MACHINE_LEARNING_ENGINEER",
        "DEEP_LEARNING_RESEARCHER",
        "COMPUTER_VISION_ENGINEER",
        "NLP_ENGINEER",
        "LLM_ENGINEER",
        "MLOPS_ENGINEER",
        "AI_EVALUATION_ENGINEER",
        "DATA_SCIENTIST",
        "GPU_HPC_ENGINEER",
    ),
    "ECONOMICS_FINANCE": (
        "ECONOMIST",
        "FINANCIAL_ANALYST",
        "INVESTMENT_ANALYST",
        "QUANTITATIVE_ANALYST",
        "FINANCIAL_MODELING",
        "RISK_ANALYST",
        "CORPORATE_FINANCE",
        "VALUATION_SPECIALIST",
        "ACCOUNTING_SPECIALIST",
        "MARKET_RESEARCH_ANALYST",
    ),
    "BUSINESS_PRODUCT": (
        "PRODUCT_MANAGER",
        "BUSINESS_ANALYST",
        "BUSINESS_STRATEGIST",
        "PROJECT_MANAGER",
        "OPERATIONS_MANAGER",
        "GROWTH_SPECIALIST",
        "MARKET_RESEARCHER",
    ),
    "RESEARCH_SCIENCE": (
        "RESEARCH_SCIENTIST",
        "RESEARCH_METHODOLOGIST",
        "STATISTICIAN",
        "EXPERIMENTAL_DESIGNER",
        "LITERATURE_REVIEWER",
        "REPRODUCIBILITY_AUDITOR",
    ),
    "LEGAL_COMPLIANCE": (
        "LEGAL_RESEARCHER",
        "CONTRACT_ANALYST",
        "COMPLIANCE_SPECIALIST",
        "PRIVACY_SPECIALIST",
        "REGULATORY_ANALYST",
        "INTELLECTUAL_PROPERTY_SPECIALIST",
    ),
    "DESIGN_CREATIVE": (
        "PRODUCT_DESIGNER",
        "UX_RESEARCHER",
        "UI_DESIGNER",
        "VISUAL_DESIGNER",
        "BRAND_DESIGNER",
        "MOTION_DESIGNER",
        "CONTENT_STRATEGIST",
    ),
    "HEALTHCARE_LIFE_SCIENCES": (
        "CLINICAL_RESEARCHER",
        "MEDICAL_LITERATURE_REVIEWER",
        "PUBLIC_HEALTH_ANALYST",
        "BIOMEDICAL_RESEARCHER",
        "HEALTHCARE_DATA_ANALYST",
        "PATIENT_SAFETY_REVIEWER",
    ),
    "DATA_ANALYTICS": (
        "DATA_ARCHITECT",
        "DATA_ENGINEER",
        "ANALYTICS_ENGINEER",
        "BI_ANALYST",
        "DATA_QUALITY_ENGINEER",
        "DATA_GOVERNANCE_SPECIALIST",
        "DATA_VISUALIZATION_SPECIALIST",
    ),
    "MANUFACTURING_INDUSTRIAL": (
        "INDUSTRIAL_SYSTEMS_ENGINEER",
        "MANUFACTURING_PROCESS_ENGINEER",
        "QUALITY_CONTROL_SIX_SIGMA",
        "OT_ICS_ENGINEER",
        "MAINTENANCE_RELIABILITY_ENGINEER",
    ),
    "ROBOTICS_AUTOMATION": (
        "ROBOTICS_SYSTEMS_ARCHITECT",
        "CONTROLS_AND_KINEMATICS_ENGINEER",
        "AUTONOMOUS_NAVIGATION_SLAM_ENGINEER",
        "EMBEDDED_FIRMWARE_ENGINEER",
        "ROBOTICS_SAFETY_VALIDATION_ENGINEER",
    ),
    "SUPPLY_CHAIN_LOGISTICS": (
        "SUPPLY_CHAIN_STRATEGIST",
        "DEMAND_FORECASTING_PLANNER",
        "LOGISTICS_NETWORK_OPTIMIZER",
        "PROCUREMENT_SOURCING_SPECIALIST",
        "INVENTORY_WAREHOUSE_ANALYST",
    ),
    "ENERGY_SUSTAINABILITY": (
        "ENERGY_SYSTEMS_ANALYST",
        "GRID_AND_POWER_SYSTEMS_ENGINEER",
        "RENEWABLE_ENERGY_SPECIALIST",
        "ESG_CARBON_ACCOUNTING_ANALYST",
        "ENVIRONMENTAL_COMPLIANCE_SPECIALIST",
    ),
    "EDUCATION_TRAINING": (
        "INSTRUCTIONAL_DESIGNER",
        "CURRICULUM_ARCHITECT",
        "ASSESSMENT_PSYCHOMETRIC_SPECIALIST",
        "TECHNICAL_TRAINER",
        "LEARNING_EXPERIENCE_EVALUATOR",
    ),
}

CROSS_DOMAIN_SKILLS: Tuple[str, ...] = (
    "COGNITIVE_EXECUTION",
    "CRITICAL_THINKING",
    "SYSTEMS_THINKING",
    "RESEARCH_AND_SOURCE_VALIDATION",
    "DATA_INTERPRETATION",
    "DECISION_ANALYSIS",
    "TECHNICAL_WRITING",
    "DOCUMENTATION",
    "QUALITY_ASSURANCE",
    "RISK_MANAGEMENT",
    "COMMUNICATION",
    "REQUIREMENTS_ANALYSIS",
)

SPECIALIZED_SKILLS: Tuple[str, ...] = (
    "HUMAN_CENTRIC_APPLICATION_QA",
    "BROWSER_AND_GUI_INTERACTION",
    "API_TESTING",
    "DATABASE_VALIDATION",
    "PERFORMANCE_BENCHMARKING",
    "SECURITY_ASSESSMENT",
    "FINANCIAL_MODEL_VALIDATION",
    "SCIENTIFIC_REPRODUCIBILITY",
    "MODEL_EVALUATION",
    "SKILL_DISCOVERY_AND_LOADING",
)

TEMPLATE_FILES: Tuple[str, ...] = (
    "PROJECT_MANIFEST.md",
    "PROJECT_STATE.md",
    "AGENT_COMMUNICATE.md",
    "WORKER_REGISTRY.md",
    "WORKER_ASSIGNMENT.md",
    "WORKSTREAM_CONTRACT.md",
    "HANDOFF_REPORT.md",
    "TECHNICAL_REVIEW.md",
    "BUSINESS_REVIEW.md",
    "QA_REPORT.md",
    "RISK_REGISTER.md",
    "FINAL_DELIVERY.md",
)

SUBAGENT_PROMPT_FILES: Tuple[str, ...] = (
    "SUBAGENT_CREATION_PROMPT.md",
    "DOMAIN_WORKER_PROMPT.md",
    "RESEARCH_AGENT_PROMPT.md",
    "IMPLEMENTATION_AGENT_PROMPT.md",
    "QA_AGENT_PROMPT.md",
    "SECURITY_AGENT_PROMPT.md",
    "REVIEWER_AGENT_PROMPT.md",
)

EXAMPLE_FILES: Tuple[str, ...] = (
    "SIMPLE_TASK.md",
    "MODERATE_TASK.md",
    "COMPLEX_SOFTWARE_PROJECT.md",
    "AI_ML_PROJECT.md",
    "CYBERSECURITY_ASSESSMENT.md",
    "FINANCIAL_ANALYSIS.md",
    "MULTI_DOMAIN_PROJECT.md",
)

SKILL_MANDATORY_LABELS: Tuple[Tuple[str, str], ...] = (
    ("Skill ID", r"skill\s+id"),
    ("Name", r"\bname\b"),
    ("Domain", r"\bdomain\b"),
    ("Version", r"\bversion\b"),
    ("Purpose", r"\bpurpose\b"),
    ("Required Competencies", r"required\s+competencies"),
    ("Prerequisites", r"\bprerequisites\b"),
    ("Workflow", r"\bworkflow\b"),
    ("Tools and Techniques", r"tools\s+(?:and|&)\s+techniques"),
    ("Verification Requirements", r"verification\s+requirements"),
    ("Quality Criteria", r"quality\s+criteria"),
    ("Security and Ethical Boundaries", r"security\s+(?:and|&)\s+ethical\s+boundaries"),
    ("Expected Deliverables", r"expected\s+deliverables"),
)

ROLE_PROMPT_REQUIRED_PATTERNS: Tuple[Tuple[str, str], ...] = (
    ("Role Identity / Domain Scope", r"(?:role\s+identity|role\s+id|domain\s+scope)"),
    ("Core Competencies & Standards", r"(?:competenc|professional\s+standard)"),
    ("When to Select Criteria", r"when\s+to\s+select"),
    ("When NOT to Select Criteria", r"when\s+not\s+to\s+select"),
    ("Multi-Role Compatibility Note", r"(?:multi-role|compatible\s+role|role\s+compatibility|co-locat)"),
    ("Decision Criteria / Reasoning Framework", r"(?:decision\s+criteria|reasoning\s+framework)"),
    ("Workflow & Expected Deliverables", r"(?=[\s\S]*workflow)(?=[\s\S]*deliverable)"),
    ("Failure Modes / Anti-Patterns", r"(?:failure\s+mode|anti-pattern)"),
    ("Quality Gates & Verification", r"(?:quality\s+gate|independent\s+verification|verification\s+method)"),
    ("Tools & Runtime Compatibility", r"(?=[\s\S]*\btool)(?=[\s\S]*runtime)"),
    (
        "Ethical / Safety / Security Boundaries",
        r"(?:ethical|safety|security|regulatory)[\s\S]{0,120}(?:boundar|guardrail|constraint|compliance|governance|policy|standard)",
    ),
)

AGENT_COMMUNICATE_15_SECTIONS: Tuple[Tuple[str, str], ...] = (
    ("1. Project Identity", r"project\s+identity"),
    ("2. Mission & Objectives", r"mission\s*(?:&|and)\s*objectives"),
    ("3. PM & SA Ownership", r"pm\s*(?:&|and|\+)\s*sa\s+ownership"),
    ("4. Current Project Status", r"current\s+project\s+status"),
    ("5. Acceptance Criteria", r"acceptance\s+criteria"),
    ("6. Worker Registry", r"worker\s+registry"),
    ("7. Workstream Ownership", r"workstream\s+ownership"),
    ("8. File Ownership", r"file\s+ownership"),
    ("9. Decisions & Rationale", r"decisions\s*(?:&|and)\s*rationale"),
    ("10. Dependencies & Blockers", r"dependencies\s*(?:&|and)\s*blockers"),
    ("11. Event & Handoff Log", r"event\s*(?:&|and)\s*handoff\s+log"),
    ("12. Technical Signoff", r"technical\s+sign-?off"),
    ("13. Business/UX Signoff", r"business\s*(?:/|&|and)\s*ux\s+sign-?off"),
    ("14. Outstanding Issues", r"outstanding\s+issues"),
    ("15. Next Actions", r"next\s+actions"),
)

SUBAGENT_CREATION_16_FIELDS: Tuple[Tuple[str, str], ...] = (
    ("1. Agent Identity", r"agent\s+identity"),
    ("2. Assigned Role / Compatible Roles", r"assigned\s+role.*compatible\s+roles|compatible\s+roles"),
    ("3. Domain", r"\bdomain\b"),
    ("4. Workstream", r"\bworkstream\b"),
    ("5. Objective", r"\bobjective\b"),
    ("6. Scope", r"\bscope\b"),
    ("7. Required Context", r"required\s+context"),
    ("8. Loaded Skills", r"loaded\s+skills"),
    ("9. Inputs", r"\binputs\b"),
    ("10. Expected Outputs", r"expected\s+outputs"),
    ("11. Dependencies", r"\bdependencies\b"),
    ("12. File Ownership", r"file\s+ownership"),
    ("13. Tool Permissions", r"tool\s+permissions"),
    ("14. Acceptance Criteria", r"acceptance\s+criteria"),
    ("15. Verification Requirements", r"verification\s+requirements"),
    ("16. Reporting & Handoff Format", r"reporting\s*(?:&|and)\s*handoff\s+format"),
)

FENCED_BLOCK_RE = re.compile(r"(^|\n)(`{3,}|~{3,})[^\n]*\n[\s\S]*?\n\2[ \t]*(?=\n|$)")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
MD_LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)\n]+)\)")
KEBAB_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
EMOJI_RE = re.compile(r"[\U0001F300-\U0001FAFF\u2728\u26A1\U0001F916]")
NEGATION_CONTEXT_RE = re.compile(
    r"\b(?:zero|no|not|never|forbid\w*|prohibit\w*|avoid\w*|without|reject\w*|absent|disallow\w*|anti-pattern\w*|superficial|free\s+of|instead\s+of|rather\s+than)\b",
    re.IGNORECASE,
)
PLACEHOLDER_UPPER_RE = re.compile(r"\b(?:TODO|TBD|FIXME)\b")
PLACEHOLDER_PHRASE_RE = re.compile(
    r"(?:\[(?:todo|tbd|fixme|insert\s+here)\]|\b(?:todo|tbd|fixme)\s*:|\blorem\s+ipsum\b|\bcoming\s+soon\b)",
    re.IGNORECASE,
)
SUPERFICIAL_PROMPT_RE = re.compile(
    r"\b(?:act\s+as\s+an?\s+expert|you\s+are\s+a\s+world-class\s+genius|act\s+like\s+an?\s+expert)\b",
    re.IGNORECASE,
)


@dataclass
class ValidationReport:
    """Aggregates validation errors across categories."""

    root: Path
    errors: List[str] = field(default_factory=list)
    checked_files: Set[Path] = field(default_factory=set)
    optional_files: Set[Path] = field(default_factory=set)

    def fail(self, category: str, rel_path: str, message: str) -> None:
        self.errors.append(f"[{category}] {rel_path}: {message}")


def strip_code_segments(markdown_text: str) -> str:
    """Remove fenced code blocks and inline code spans while preserving structure."""
    without_fences = FENCED_BLOCK_RE.sub("\n", markdown_text)
    return INLINE_CODE_RE.sub("", without_fences)


def parse_yaml_frontmatter(text: str) -> Tuple[Dict[str, str] | None, str, str | None]:
    """Parse simple YAML frontmatter at byte 0 without external dependencies."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return None, text, "File does not start with YAML frontmatter delimiter '---' on line 1"

    lines = text.splitlines()
    end_idx = None
    for idx in range(1, len(lines)):
        if lines[idx].strip() == "---":
            end_idx = idx
            break

    if end_idx is None:
        return None, text, "Unclosed YAML frontmatter (missing closing '---')"

    fm_lines = lines[1:end_idx]
    body = "\n".join(lines[end_idx + 1 :])
    data: Dict[str, str] = {}
    i = 0
    while i < len(fm_lines):
        raw = fm_lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        if ":" not in raw or raw.startswith((" ", "\t")):
            return None, body, f"Invalid YAML frontmatter line {i + 2}: {raw!r}"
        key, val = raw.split(":", 1)
        key = key.strip()
        val = val.strip()
        if val in (">", "|", ">-", "|-"):
            folded: List[str] = []
            i += 1
            while i < len(fm_lines) and (fm_lines[i].startswith((" ", "\t")) or not fm_lines[i].strip()):
                if fm_lines[i].strip():
                    folded.append(fm_lines[i].strip())
                i += 1
            data[key] = " ".join(folded).strip()
            continue
        if len(val) >= 2 and ((val[0] == val[-1] == '"') or (val[0] == val[-1] == "'")):
            val = val[1:-1]
        data[key] = val
        i += 1

    return data, body, None


def check_file_thresholds(
    report: ValidationReport,
    category: str,
    file_path: Path,
    min_lines: int,
    min_bytes: int,
    max_bytes: int | None = None,
    is_optional: bool = False,
) -> str | None:
    """Verify file existence, UTF-8 readability, and line/byte bounds."""
    rel = file_path.relative_to(report.root).as_posix()
    if not file_path.is_file():
        if not is_optional:
            report.fail(category, rel, "Missing required file")
        return None

    if is_optional:
        report.optional_files.add(file_path.resolve())
    else:
        report.checked_files.add(file_path.resolve())
    try:
        raw_bytes = file_path.read_bytes()
        content = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        report.fail(category, rel, f"Invalid UTF-8 encoding: {exc}")
        return None

    byte_len = len(raw_bytes)
    line_count = len(content.splitlines())
    if line_count < min_lines:
        report.fail(category, rel, f"Insufficient line depth ({line_count} lines < required {min_lines})")
    if byte_len < min_bytes:
        report.fail(category, rel, f"Insufficient content depth ({byte_len} bytes < required {min_bytes})")
    if max_bytes is not None and byte_len > max_bytes:
        report.fail(category, rel, f"Exceeds maximum rule size cap ({byte_len} bytes > {max_bytes} bytes)")
    return content


def check_unexpected_children(
    report: ValidationReport,
    category: str,
    directory: Path,
    expected_names: Sequence[str],
) -> None:
    """Ensure canonical library folders do not contain stray/misnamed files or directories."""
    if not directory.is_dir():
        return
    expected_set = set(expected_names)
    for child in sorted(directory.iterdir()):
        if child.name == ".DS_Store":
            continue
        if child.name not in expected_set:
            report.fail(
                category,
                child.relative_to(report.root).as_posix(),
                f"Unexpected non-canonical entry inside {directory.name}/",
            )


def validate_root_files(report: ValidationReport) -> None:
    for fname in ("README.md", "LIBRARY_INDEX.md", "CHANGELOG.md"):
        text = check_file_thresholds(report, "ROOT", report.root / fname, min_lines=25, min_bytes=900)
        if fname == "LIBRARY_INDEX.md" and text is not None:
            if "AUTONOMOUS_ORCHESTRATION.md" not in text:
                report.fail(
                    "ROOT",
                    "LIBRARY_INDEX.md",
                    "LIBRARY_INDEX.md must index 01_ORCHESTRATION/AUTONOMOUS_ORCHESTRATION.md",
                )

    version_text = check_file_thresholds(report, "ROOT", report.root / "VERSION.md", min_lines=1, min_bytes=5)
    if version_text is not None and "1.0.0" not in version_text:
        report.fail("ROOT", "VERSION.md", "VERSION.md must lock semantic version '1.0.0'")

    skills_json_path = report.root / "skills.json"
    if not skills_json_path.is_file():
        report.fail("ROOT", "skills.json", "Missing required root file skills.json")
    else:
        report.checked_files.add(skills_json_path.resolve())


def validate_global_constitution(report: ValidationReport) -> None:
    base = report.root / "00_GLOBAL_CONSTITUTION"
    if not base.is_dir():
        report.fail("CONSTITUTION", "00_GLOBAL_CONSTITUTION", "Missing directory")
        return

    check_unexpected_children(report, "CONSTITUTION", base, GLOBAL_CONSTITUTION_FILES)
    for fname in GLOBAL_CONSTITUTION_FILES:
        text = check_file_thresholds(
            report,
            "CONSTITUTION",
            base / fname,
            min_lines=35,
            min_bytes=1400,
            max_bytes=24576,
        )
        if text is None:
            continue
        if fname == "TASK_COMPLEXITY_ROUTER.md":
            for lvl in range(5):
                if not re.search(rf"\blevel\s+{lvl}\b", text, re.IGNORECASE):
                    report.fail("CONSTITUTION", f"00_GLOBAL_CONSTITUTION/{fname}", f"Missing Level {lvl} definition")
        if fname in ("GLOBAL_SYSTEM_PROMPT.md", "AGENT_GOVERNANCE.md"):
            if not re.search(r"precedence|hierarchy|override", text, re.IGNORECASE):
                report.fail(
                    "CONSTITUTION",
                    f"00_GLOBAL_CONSTITUTION/{fname}",
                    "Must explicitly define instruction precedence / override rules",
                )


def validate_orchestration(report: ValidationReport) -> None:
    base = report.root / "01_ORCHESTRATION"
    if not base.is_dir():
        report.fail("ORCHESTRATION", "01_ORCHESTRATION", "Missing directory")
        return

    check_unexpected_children(report, "ORCHESTRATION", base, ORCHESTRATION_FILES)
    for fname in ORCHESTRATION_FILES:
        min_l = 55 if fname == "AUTONOMOUS_ORCHESTRATION.md" else 35
        min_b = 2200 if fname == "AUTONOMOUS_ORCHESTRATION.md" else 1400
        text = check_file_thresholds(
            report,
            "ORCHESTRATION",
            base / fname,
            min_lines=min_l,
            min_bytes=min_b,
            max_bytes=24576,
        )
        if text is None:
            continue
        if fname == "DYNAMIC_AGENT_ALLOCATION.md":
            if not (re.search(r"\brole\b", text, re.IGNORECASE) and re.search(r"\bagent\b", text, re.IGNORECASE)):
                report.fail(
                    "ORCHESTRATION",
                    f"01_ORCHESTRATION/{fname}",
                    "Must distinguish logical Role from runtime Agent",
                )
        if fname == "AUTONOMOUS_ORCHESTRATION.md":
            rel_ao = f"01_ORCHESTRATION/{fname}"
            norm_text = re.sub(r"\s+", " ", text)
            if not re.search(r"natural[- ]language", text, re.IGNORECASE):
                report.fail("ORCHESTRATION", rel_ao, "Missing natural-language interaction principle")
            if not (re.search(r"\bINIT\b", text) and re.search(r"\bCONTINUE\b", text)):
                report.fail("ORCHESTRATION", rel_ao, "Must explicitly forbid requiring command modes (INIT / CONTINUE)")
            for phase_name in AUTONOMOUS_13_PHASES:
                if not re.search(re.escape(phase_name), norm_text, re.IGNORECASE):
                    report.fail("ORCHESTRATION", rel_ao, f"Missing required internal autonomous phase: '{phase_name}'")
            if not re.search(r"\bcheckpoint\b", text, re.IGNORECASE):
                report.fail("ORCHESTRATION", rel_ao, "Missing checkpoint auto-resume coverage")
            if not (
                re.search(r"\bsequential\b", text, re.IGNORECASE)
                and re.search(r"PROJECT_STATE\.md|state[- ]file", text, re.IGNORECASE)
            ):
                report.fail("ORCHESTRATION", rel_ao, "Missing runtime sequential and state-file fallback rules")
            if not re.search(r"ordinary[- ]language|plain[- ]language|concise", text, re.IGNORECASE):
                report.fail("ORCHESTRATION", rel_ao, "Missing ordinary-language user communication policy")
            if not re.search(
                r"The user gives objectives\.\s*PM manages execution\.\s*SA governs architecture\.",
                norm_text,
                re.IGNORECASE,
            ):
                report.fail(
                    "ORCHESTRATION",
                    rel_ao,
                    "Missing verbatim Final Interaction Rule ('The user gives objectives. PM manages execution. SA governs architecture. ...')",
                )


def _validate_role_prompt_content(report: ValidationReport, category: str, prompt_path: Path, text: str) -> None:
    rel = prompt_path.relative_to(report.root).as_posix()
    for label, pattern in ROLE_PROMPT_REQUIRED_PATTERNS:
        if not re.search(pattern, text, re.IGNORECASE):
            report.fail(category, rel, f"Missing required role section/coverage: {label}")


def validate_core_roles(report: ValidationReport) -> None:
    base = report.root / "02_CORE_ROLES"
    if not base.is_dir():
        report.fail("CORE_ROLES", "02_CORE_ROLES", "Missing directory")
        return

    check_unexpected_children(report, "CORE_ROLES", base, CORE_ROLES)
    for role in CORE_ROLES:
        role_dir = base / role
        if not role_dir.is_dir():
            report.fail("CORE_ROLES", f"02_CORE_ROLES/{role}", "Missing core role directory")
            continue
        check_unexpected_children(report, "CORE_ROLES", role_dir, ("SYSTEM_PROMPT.md", "QUALITY_CHECKLIST.md"))
        sp_text = check_file_thresholds(
            report, "CORE_ROLES", role_dir / "SYSTEM_PROMPT.md", min_lines=45, min_bytes=1800, max_bytes=24576
        )
        if sp_text is not None:
            _validate_role_prompt_content(report, "CORE_ROLES", role_dir / "SYSTEM_PROMPT.md", sp_text)
            if role == "PROJECT_MANAGER":
                rel_pm = "02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md"
                if not (
                    re.search(r"\bautonomous\b", sp_text, re.IGNORECASE)
                    and re.search(r"\b(?:phase|checkpoint|batch)\b", sp_text, re.IGNORECASE)
                ):
                    report.fail("CORE_ROLES", rel_pm, "PM prompt must reference autonomous phase/batch/checkpoint orchestration")
                if not re.search(r"natural[- ]language|operational\s+burden", sp_text, re.IGNORECASE):
                    report.fail(
                        "CORE_ROLES",
                        rel_pm,
                        "PM prompt must enforce zero user operational burden / natural-language interaction",
                    )
        check_file_thresholds(
            report, "CORE_ROLES", role_dir / "QUALITY_CHECKLIST.md", min_lines=18, min_bytes=900, max_bytes=24576
        )


def validate_domains_and_roles(report: ValidationReport) -> None:
    base = report.root / "03_DOMAINS"
    if not base.is_dir():
        report.fail("DOMAINS", "03_DOMAINS", "Missing directory")
        return

    check_unexpected_children(report, "DOMAINS", base, tuple(DOMAIN_ROLES.keys()))
    for domain, roles in DOMAIN_ROLES.items():
        dom_dir = base / domain
        if not dom_dir.is_dir():
            report.fail("DOMAINS", f"03_DOMAINS/{domain}", "Missing domain directory")
            continue

        check_unexpected_children(
            report,
            "DOMAINS",
            dom_dir,
            ("DOMAIN_INDEX.md", "DOMAIN_SYSTEM_PROMPT.md", "QUALITY_GATES.md", "ROLES"),
        )
        idx_text = check_file_thresholds(
            report, "DOMAINS", dom_dir / "DOMAIN_INDEX.md", min_lines=35, min_bytes=1400, max_bytes=24576
        )
        check_file_thresholds(
            report, "DOMAINS", dom_dir / "DOMAIN_SYSTEM_PROMPT.md", min_lines=45, min_bytes=1800, max_bytes=24576
        )
        check_file_thresholds(
            report, "DOMAINS", dom_dir / "QUALITY_GATES.md", min_lines=35, min_bytes=1400, max_bytes=24576
        )

        if idx_text is not None:
            for role in roles:
                if role not in idx_text:
                    report.fail(
                        "DOMAINS",
                        f"03_DOMAINS/{domain}/DOMAIN_INDEX.md",
                        f"DOMAIN_INDEX.md does not reference canonical role '{role}'",
                    )

        roles_dir = dom_dir / "ROLES"
        if not roles_dir.is_dir():
            report.fail("DOMAINS", f"03_DOMAINS/{domain}/ROLES", "Missing ROLES directory")
            continue

        check_unexpected_children(report, "DOMAINS", roles_dir, roles)
        is_cyber = domain == "CYBERSECURITY"
        for role in roles:
            role_dir = roles_dir / role
            if not role_dir.is_dir():
                report.fail("DOMAINS", f"03_DOMAINS/{domain}/ROLES/{role}", "Missing role directory")
                continue

            expected_role_files = (
                ("SYSTEM_PROMPT.md", "QUALITY_CHECKLIST.md", "WORKFLOW.md")
                if is_cyber
                else ("SYSTEM_PROMPT.md", "QUALITY_CHECKLIST.md")
            )
            allowed_role_files = ("SYSTEM_PROMPT.md", "QUALITY_CHECKLIST.md", "WORKFLOW.md")
            check_unexpected_children(report, "DOMAINS", role_dir, allowed_role_files)

            sp_path = role_dir / "SYSTEM_PROMPT.md"
            sp_text = check_file_thresholds(
                report, "DOMAINS", sp_path, min_lines=45, min_bytes=1800, max_bytes=24576
            )
            qc_text = check_file_thresholds(
                report, "DOMAINS", role_dir / "QUALITY_CHECKLIST.md", min_lines=18, min_bytes=900, max_bytes=24576
            )
            wf_text = None
            if is_cyber:
                wf_text = check_file_thresholds(
                    report, "DOMAINS", role_dir / "WORKFLOW.md", min_lines=25, min_bytes=1300, max_bytes=24576
                )
            elif (role_dir / "WORKFLOW.md").exists():
                wf_text = check_file_thresholds(
                    report,
                    "DOMAINS",
                    role_dir / "WORKFLOW.md",
                    min_lines=25,
                    min_bytes=1300,
                    max_bytes=24576,
                    is_optional=True,
                )

            if sp_text is not None:
                _validate_role_prompt_content(report, "DOMAINS", sp_path, sp_text)

            if is_cyber and sp_text is not None:
                combined = "\n".join(part for part in (sp_text, qc_text or "", wf_text or "") if part)
                rel_sp = sp_path.relative_to(report.root).as_posix()
                if not re.search(r"\bauthoriz(?:ation|ed)\b", sp_text, re.IGNORECASE):
                    report.fail("CYBER_SAFETY", rel_sp, "Missing explicit authorization requirement")
                if not re.search(r"rules\s+of\s+engagement|\bRoE\b", combined, re.IGNORECASE):
                    report.fail("CYBER_SAFETY", rel_sp, "Missing explicit Rules of Engagement (RoE) requirement")
                if not re.search(r"\bscope\b", sp_text, re.IGNORECASE):
                    report.fail("CYBER_SAFETY", rel_sp, "Missing explicit target scope boundary requirement")
                if not re.search(r"non-destructive|safe|out-of-scope|halt|escalat", sp_text, re.IGNORECASE):
                    report.fail("CYBER_SAFETY", rel_sp, "Missing non-destructive / halt-on-breach safety control")


def _validate_skill_package(
    report: ValidationReport,
    layer_dir_name: str,
    skill_dir_name: str,
    expected_id_prefix: str,
) -> str | None:
    skill_dir = report.root / layer_dir_name / skill_dir_name
    rel_dir = f"{layer_dir_name}/{skill_dir_name}"
    if not skill_dir.is_dir():
        report.fail("SKILLS", rel_dir, "Missing skill directory")
        return None

    check_unexpected_children(report, "SKILLS", skill_dir, ("SKILL.md",))
    skill_file = skill_dir / "SKILL.md"
    rel_file = f"{rel_dir}/SKILL.md"
    text = check_file_thresholds(report, "SKILLS", skill_file, min_lines=55, min_bytes=2200, max_bytes=24576)
    if text is None:
        return None

    fm, body, fm_err = parse_yaml_frontmatter(text)
    if fm_err is not None or fm is None:
        report.fail("SKILLS", rel_file, fm_err or "Invalid YAML frontmatter")
        return None

    expected_kebab = skill_dir_name.lower().replace("_", "-")
    name_val = fm.get("name", "").strip()
    desc_val = fm.get("description", "").strip()
    if not name_val or not KEBAB_RE.match(name_val):
        report.fail("SKILLS", rel_file, f"YAML frontmatter 'name' must be kebab-case (got {name_val!r})")
    elif name_val != expected_kebab:
        report.fail(
            "SKILLS",
            rel_file,
            f"YAML frontmatter 'name' ({name_val!r}) must match directory slug ({expected_kebab!r})",
        )
    if len(desc_val) < 20:
        report.fail("SKILLS", rel_file, "YAML frontmatter 'description' must be at least 20 characters")

    for label, pattern in SKILL_MANDATORY_LABELS:
        if not re.search(pattern, body, re.IGNORECASE):
            report.fail("SKILLS", rel_file, f"Missing mandatory skill section/field: {label}")

    if expected_id_prefix not in body:
        report.fail("SKILLS", rel_file, f"Missing canonical Skill ID prefix '{expected_id_prefix}'")
    if "1.0.0" not in body and fm.get("version") != "1.0.0":
        report.fail("SKILLS", rel_file, "Missing required Version '1.0.0'")
    if re.search(r"override\s+global\s+constitution|bypass\s+authorization", body, re.IGNORECASE):
        if not NEGATION_CONTEXT_RE.search(body):
            report.fail("SKILLS", rel_file, "Skill must never claim authority to override constitution/authorization")

    if skill_dir_name == "HUMAN_CENTRIC_APPLICATION_QA":
        for lvl in (1, 2, 3):
            if not re.search(rf"\blevel\s+{lvl}\b", body, re.IGNORECASE):
                report.fail("SKILLS", rel_file, f"HUMAN_CENTRIC_APPLICATION_QA must define QA Level {lvl}")

    return name_val


def validate_skills_and_manifest(report: ValidationReport) -> None:
    cross_base = report.root / "04_CROSS_DOMAIN_SKILLS"
    spec_base = report.root / "05_SPECIALIZED_SKILLS"
    if not cross_base.is_dir():
        report.fail("SKILLS", "04_CROSS_DOMAIN_SKILLS", "Missing directory")
    else:
        check_unexpected_children(report, "SKILLS", cross_base, CROSS_DOMAIN_SKILLS)
        for sdir in CROSS_DOMAIN_SKILLS:
            _validate_skill_package(report, "04_CROSS_DOMAIN_SKILLS", sdir, "SKL-CORE-")

    if not spec_base.is_dir():
        report.fail("SKILLS", "05_SPECIALIZED_SKILLS", "Missing directory")
    else:
        check_unexpected_children(report, "SKILLS", spec_base, SPECIALIZED_SKILLS)
        for sdir in SPECIALIZED_SKILLS:
            _validate_skill_package(report, "05_SPECIALIZED_SKILLS", sdir, "SKL-SPEC-")

    skills_json_path = report.root / "skills.json"
    if not skills_json_path.is_file():
        return

    try:
        manifest = json.loads(skills_json_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.fail("SKILLS_JSON", "skills.json", f"Invalid JSON syntax: {exc}")
        return

    if not isinstance(manifest, dict):
        report.fail("SKILLS_JSON", "skills.json", "Top-level JSON value must be an object")
        return

    allowed_top_keys = {"entries", "inherits"}
    extra_top = set(manifest.keys()) - allowed_top_keys
    if extra_top:
        report.fail(
            "SKILLS_JSON",
            "skills.json",
            f"Unsupported top-level keys {sorted(extra_top)}; Antigravity skills.json allows only 'entries' and 'inherits'",
        )

    entries = manifest.get("entries")
    if not isinstance(entries, list) or not entries:
        report.fail("SKILLS_JSON", "skills.json", "'entries' must be a non-empty array of path objects")
        return

    allowed_entry_keys = {"path", "include_only", "exclude"}
    resolved_dirs: Set[str] = set()
    discovered_skills: List[Path] = []
    for idx, item in enumerate(entries):
        if not isinstance(item, dict):
            report.fail("SKILLS_JSON", "skills.json", f"entries[{idx}] must be an object")
            continue
        extra_keys = set(item.keys()) - allowed_entry_keys
        if extra_keys:
            report.fail(
                "SKILLS_JSON",
                "skills.json",
                f"entries[{idx}] contains unsupported keys {sorted(extra_keys)}",
            )
        raw_path = item.get("path")
        if not isinstance(raw_path, str) or not raw_path.strip():
            report.fail("SKILLS_JSON", "skills.json", f"entries[{idx}] missing non-empty string 'path'")
            continue
        norm_rel = raw_path.strip().lstrip("./").rstrip("/")
        target_dir = (report.root / norm_rel).resolve()
        if not target_dir.is_dir():
            report.fail("SKILLS_JSON", "skills.json", f"entries[{idx}] path '{raw_path}' does not resolve to a directory")
            continue
        resolved_dirs.add(norm_rel)
        for child in sorted(target_dir.iterdir()):
            if child.is_dir() and (child / "SKILL.md").is_file():
                discovered_skills.append(child / "SKILL.md")

    for req_dir in ("04_CROSS_DOMAIN_SKILLS", "05_SPECIALIZED_SKILLS"):
        if req_dir not in resolved_dirs:
            report.fail("SKILLS_JSON", "skills.json", f"Missing required skill directory entry '{req_dir}'")

    if "inherits" in manifest:
        inherits = manifest["inherits"]
        if not isinstance(inherits, list):
            report.fail("SKILLS_JSON", "skills.json", "'inherits' must be an array when present")
        else:
            for idx, inh in enumerate(inherits):
                if not isinstance(inh, dict) or not isinstance(inh.get("path"), str):
                    report.fail("SKILLS_JSON", "skills.json", f"inherits[{idx}] must be an object with string 'path'")

    if resolved_dirs >= {"04_CROSS_DOMAIN_SKILLS", "05_SPECIALIZED_SKILLS"} and len(discovered_skills) != 22:
        report.fail(
            "SKILLS_JSON",
            "skills.json",
            f"One-level scan across skills.json entries discovered {len(discovered_skills)} skills (expected 22)",
        )


def validate_templates(report: ValidationReport) -> None:
    base = report.root / "06_TEMPLATES"
    if not base.is_dir():
        report.fail("TEMPLATES", "06_TEMPLATES", "Missing directory")
        return

    check_unexpected_children(report, "TEMPLATES", base, TEMPLATE_FILES)
    for fname in TEMPLATE_FILES:
        text = check_file_thresholds(
            report, "TEMPLATES", base / fname, min_lines=35, min_bytes=1200, max_bytes=24576
        )
        if text is not None and fname == "AGENT_COMMUNICATE.md":
            for label, pattern in AGENT_COMMUNICATE_15_SECTIONS:
                if not re.search(pattern, text, re.IGNORECASE):
                    report.fail(
                        "TEMPLATES",
                        "06_TEMPLATES/AGENT_COMMUNICATE.md",
                        f"Missing mandatory section in AGENT_COMMUNICATE.md: {label}",
                    )
        if text is not None and fname == "PROJECT_STATE.md":
            if not re.search(r"research\s+queue", text, re.IGNORECASE):
                report.fail("TEMPLATES", "06_TEMPLATES/PROJECT_STATE.md", "Missing mandatory 'Research Queue' tracking section")
            if not re.search(r"\bcheckpoint\b", text, re.IGNORECASE):
                report.fail("TEMPLATES", "06_TEMPLATES/PROJECT_STATE.md", "Missing mandatory 'Checkpoint' tracking section")


def validate_subagent_prompts(report: ValidationReport) -> None:
    base = report.root / "07_SUBAGENT_PROMPTS"
    if not base.is_dir():
        report.fail("SUBAGENT_PROMPTS", "07_SUBAGENT_PROMPTS", "Missing directory")
        return

    check_unexpected_children(report, "SUBAGENT_PROMPTS", base, SUBAGENT_PROMPT_FILES)
    for fname in SUBAGENT_PROMPT_FILES:
        text = check_file_thresholds(
            report, "SUBAGENT_PROMPTS", base / fname, min_lines=40, min_bytes=1500, max_bytes=24576
        )
        if text is not None and fname == "SUBAGENT_CREATION_PROMPT.md":
            for label, pattern in SUBAGENT_CREATION_16_FIELDS:
                if not re.search(pattern, text, re.IGNORECASE):
                    report.fail(
                        "SUBAGENT_PROMPTS",
                        "07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md",
                        f"Missing mandatory specification field: {label}",
                    )


def validate_examples(report: ValidationReport) -> None:
    base = report.root / "08_EXAMPLES"
    if not base.is_dir():
        report.fail("EXAMPLES", "08_EXAMPLES", "Missing directory")
        return

    check_unexpected_children(report, "EXAMPLES", base, EXAMPLE_FILES)
    for fname in EXAMPLE_FILES:
        check_file_thresholds(report, "EXAMPLES", base / fname, min_lines=55, min_bytes=2200)


def iter_canonical_markdown_files(root: Path) -> List[Path]:
    """Return all existing canonical Markdown files in the library (excluding configs/ and scripts/)."""
    md_files: List[Path] = []
    for fname in ROOT_FILES:
        p = root / fname
        if p.suffix == ".md" and p.is_file():
            md_files.append(p)

    layer_dirs = (
        "00_GLOBAL_CONSTITUTION",
        "01_ORCHESTRATION",
        "02_CORE_ROLES",
        "03_DOMAINS",
        "04_CROSS_DOMAIN_SKILLS",
        "05_SPECIALIZED_SKILLS",
        "06_TEMPLATES",
        "07_SUBAGENT_PROMPTS",
        "08_EXAMPLES",
    )
    for ldir in layer_dirs:
        dpath = root / ldir
        if dpath.is_dir():
            md_files.extend(sorted(dpath.rglob("*.md")))
    return md_files


def validate_hygiene_and_links(report: ValidationReport) -> None:
    root_resolved = report.root.resolve()
    for md_path in iter_canonical_markdown_files(report.root):
        rel = md_path.relative_to(report.root).as_posix()
        try:
            raw_text = md_path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue

        stripped = strip_code_segments(raw_text)
        is_template_layer = rel.startswith(("06_TEMPLATES/", "07_SUBAGENT_PROMPTS/"))

        for line_no, line in enumerate(stripped.splitlines(), start=1):
            if (PLACEHOLDER_UPPER_RE.search(line) or PLACEHOLDER_PHRASE_RE.search(line)) and not NEGATION_CONTEXT_RE.search(line):
                report.fail("HYGIENE", f"{rel}:{line_no}", f"Forbidden unfinished placeholder in line: {line.strip()!r}")
            if SUPERFICIAL_PROMPT_RE.search(line) and not NEGATION_CONTEXT_RE.search(line):
                report.fail("HYGIENE", f"{rel}:{line_no}", f"Forbidden superficial prompt phrase in line: {line.strip()!r}")
            if EMOJI_RE.search(line):
                report.fail("HYGIENE", f"{rel}:{line_no}", "Forbidden decorative emoji ('AI Sign' clutter)")

        for match in MD_LINK_RE.finditer(stripped):
            raw_target = match.group(2).strip()
            if not raw_target:
                continue
            if " " in raw_target and not raw_target.startswith("<"):
                raw_target = raw_target.split(" ", 1)[0]
            if raw_target.startswith("<") and raw_target.endswith(">"):
                if is_template_layer:
                    continue
                raw_target = raw_target[1:-1]

            if raw_target.startswith(("#", "http://", "https://", "mailto:", "file://", "conversation://")):
                continue
            if is_template_layer and ("{{" in raw_target or ("<" in raw_target and ">" in raw_target)):
                continue

            clean_target = unquote(raw_target.split("#", 1)[0].split("?", 1)[0]).strip()
            if not clean_target:
                continue

            resolved = (md_path.parent / clean_target).resolve()
            try:
                resolved.relative_to(root_resolved)
            except ValueError:
                report.fail("LINKS", rel, f"Relative link escapes library root: {raw_target!r}")
                continue

            if not resolved.exists():
                report.fail("LINKS", rel, f"Broken relative Markdown link target: {raw_target!r}")


def run_full_validation(root: Path = LIBRARY_ROOT_DEFAULT) -> ValidationReport:
    report = ValidationReport(root=root)
    validate_root_files(report)
    validate_global_constitution(report)
    validate_orchestration(report)
    validate_core_roles(report)
    validate_domains_and_roles(report)
    validate_skills_and_manifest(report)
    validate_templates(report)
    validate_subagent_prompts(report)
    validate_examples(report)
    validate_hygiene_and_links(report)
    return report


# ---------------------------------------------------------------------------
# Pytest Entrypoints
# ---------------------------------------------------------------------------


def _assert_no_errors(report: ValidationReport) -> None:
    if report.errors:
        preview = "\n".join(report.errors[:50])
        suffix = f"\n... ({len(report.errors) - 50} additional errors)" if len(report.errors) > 50 else ""
        raise AssertionError(f"Library validation failed with {len(report.errors)} error(s):\n{preview}{suffix}")


def test_canonical_inventory_counts() -> None:
    assert len(ROOT_FILES) == 5
    assert len(GLOBAL_CONSTITUTION_FILES) == 8
    assert len(ORCHESTRATION_FILES) == 13
    assert len(CORE_ROLES) == 4
    assert len(DOMAIN_ROLES) == 15
    assert sum(len(roles) for roles in DOMAIN_ROLES.values()) == 108
    assert len(CROSS_DOMAIN_SKILLS) == 12
    assert len(SPECIALIZED_SKILLS) == 10
    assert len(TEMPLATE_FILES) == 12
    assert len(SUBAGENT_PROMPT_FILES) == 7
    assert len(EXAMPLE_FILES) == 7
    total_expected = (
        len(ROOT_FILES)
        + len(GLOBAL_CONSTITUTION_FILES)
        + len(ORCHESTRATION_FILES)
        + len(CORE_ROLES) * 2
        + len(DOMAIN_ROLES) * 3
        + sum(len(roles) * 2 for roles in DOMAIN_ROLES.values())
        + len(DOMAIN_ROLES["CYBERSECURITY"])
        + len(CROSS_DOMAIN_SKILLS)
        + len(SPECIALIZED_SKILLS)
        + len(TEMPLATE_FILES)
        + len(SUBAGENT_PROMPT_FILES)
        + len(EXAMPLE_FILES)
    )
    assert total_expected == CANONICAL_FILE_COUNT == 356


def test_library_full_validation() -> None:
    report = run_full_validation(LIBRARY_ROOT_DEFAULT)
    _assert_no_errors(report)
    assert len(report.checked_files) == CANONICAL_FILE_COUNT, (
        f"Expected {CANONICAL_FILE_COUNT} canonical files, checked {len(report.checked_files)}"
    )


# ---------------------------------------------------------------------------
# CLI Entrypoint
# ---------------------------------------------------------------------------


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the Centralized Agent System Instruction Library.")
    parser.add_argument(
        "--root",
        type=Path,
        default=LIBRARY_ROOT_DEFAULT,
        help="Path to the library root directory (defaults to parent of scripts/).",
    )
    args = parser.parse_args(argv)

    root = args.root.resolve()
    report = run_full_validation(root)

    print("=" * 76)
    print("SA LIBRARY VALIDATION SUITE — EXECUTION SUMMARY")
    print("=" * 76)
    print(f"Library Root          : {root}")
    print(f"Canonical Files Found : {len(report.checked_files)} / {CANONICAL_FILE_COUNT}")
    print(f"Validation Errors     : {len(report.errors)}")
    print("-" * 76)

    if report.errors:
        for err in report.errors:
            print(f"FAIL  {err}")
        print("-" * 76)
        print("RESULT: FAIL (SA_GATE = BLOCKED)")
        return 1

    if len(report.checked_files) != CANONICAL_FILE_COUNT:
        print(f"FAIL  Expected {CANONICAL_FILE_COUNT} canonical library files, verified {len(report.checked_files)}")
        print("RESULT: FAIL (SA_GATE = BLOCKED)")
        return 1

    print(
        f"RESULT: PASS ({CANONICAL_FILE_COUNT}/{CANONICAL_FILE_COUNT} canonical files verified; "
        "0 schema, hygiene, or link errors)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
