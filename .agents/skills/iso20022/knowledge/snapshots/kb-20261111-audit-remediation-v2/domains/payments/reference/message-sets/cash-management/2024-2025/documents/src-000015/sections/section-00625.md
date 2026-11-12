---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.8 Date Time Period", "37.1.8.1 DateTimePeriod1", "37.1.8.1.1 FromDateTime <FrDtTm>"]
file_pages: [802]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.8.1.1 FromDateTime <FrDtTm>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 802 to 802.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 802

```text
37.1.8.1.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the period starts.
Datatype: "ISODateTime" on page 883
37.1.8.1.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the period ends.
Datatype: "ISODateTime" on page 883
37.1.9 Financial Institution Identification
37.1.9.1  ClearingSystemMemberIdentification2
Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member
of the clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 802
   MemberIdentification <MmbId> [1..1] Text 802
37.1.9.1.1  ClearingSystemIdentification <ClrSysId>
Presence: [0..1]
Definition: Specification of a pre-agreed offering between clearing agents or the channel through which
the payment instruction is processed.
ClearingSystemIdentification <ClrSysId> contains one of the following elements (see
"ClearingSystemIdentification2Choice" on page 847 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 847
Or}   Proprietary <Prtry> [1..1] Text 847
37.1.9.1.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Identification of a member of a clearing system.
Datatype: "Max35Text" on page 889
37.1.9.2  GenericFinancialIdentification1
Definition: Information related to an identification of a financial institution.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 802 February 2025
```

