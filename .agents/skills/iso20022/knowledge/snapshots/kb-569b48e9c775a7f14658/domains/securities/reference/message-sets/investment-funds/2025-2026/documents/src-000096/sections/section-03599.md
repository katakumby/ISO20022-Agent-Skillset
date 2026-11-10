---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.23 InvestorProfile2", "66.1.28.23.2 Status <Sts>"]
file_pages: [4849]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.23.2 Status <Sts>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4849 to 4849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4849

```text
66.1.28.23.2  Status <Sts>
Presence: [0..1]
Definition: Status of the profile.
Status <Sts> contains one of the following InvestorProfileStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4849
Or}   Proprietary <Prtry> [1..1] ± 4849
66.1.28.23.2.1  Code <Cd>
Presence: [1..1]
Definition: Investor profile status expressed as a code.
Datatype: "InvestorProfileStatus1Code" on page 5327
CodeName Name Definition
DISA Disabled Status of the investor profile is disabled.
DISG Disabling Status of the investor profile is in the
process of being disabled.
ENAB Enabled Status of the investor profile is enabled.
ENBG Enabling Status of the investor profile is in the
process of being enabled.
ADMI InAdmission Status of the investor profile is in
admission.
ANLY InAnalysis Status of the investor profile is in
analysis.
NAPP NotApproved Status of the investor profile is not
approved.
PSUS PartiallySuspended Status of the investor profile is partially
suspended.
PEND PendingApproval Status of the investor profile is pending
approval.
SUPS Suspended Status of the investor profile is
suspended.
66.1.28.23.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Investor profile status expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4849 May 2026
```

