---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.5 SecuritiesBalanceType7Choice", "82.1.5.5.1 Code <Cd>"]
file_pages: [2852]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.5.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2852 to 2852.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2852

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2852
Or}   Proprietary <Prtry> [1..1] ± 2853
82.1.5.5.1  Code <Cd>
Presence: [1..1]
Definition: Sub-balance expressed as an ISO 20022 code.
Datatype: "SecuritiesBalanceType13Code" on page 3293
CodeName Name Definition
BLOK Blocked Balance of financial instruments that are
blocked.
AWAS AvailableWithNoAdditionalStatus Balance of financial instruments that are
freely available with no specific
additional status.
AVAI Available Balance of financial instruments that are
available.
NOMI Registered Balance of financial instruments that are
registered (in nominee name or in the
name of the beneficial owner).
PLED Pledged Balance of securities that belong to and
is kept in the safekeeping account
indicated within this message, and that
are pledged.
REGO OutForRegistration Balance of financial instruments
currently being processed by the
institution responsible for registering the
new beneficial owner (or nominee).
RSTR Restricted Balance of financial instruments that
may only be sold under certain
conditions or require legal documents.
OTHR Unclassified Other. See Narrative.
SPOS StreetPosition Balance of financial instruments that
remain registered in the name of the
prior beneficial owner.
UNRG Unregistered Balance of securities that could not be
registered due to foreign ownership
limitation.
ISSU Issued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has been received.
QUAS QuasiIssued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has not yet been
received.
COLA EligibleForCollateralPurposes Balance of securities that are eligible for
use for collateral purposes.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2852 August 2026
```

