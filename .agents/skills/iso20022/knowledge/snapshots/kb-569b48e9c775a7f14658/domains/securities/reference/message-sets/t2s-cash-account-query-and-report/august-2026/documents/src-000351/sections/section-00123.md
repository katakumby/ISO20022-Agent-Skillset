---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.4 Date Period", "7.1.4.1 DatePeriod2", "7.1.4.1.1 FromDate <FrDt>"]
file_pages: [138]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.4.1.1 FromDate <FrDt>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 138 to 138.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 138

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 138
   ToDate <ToDt> [1..1] Date 138
7.1.4.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 179
7.1.4.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 179
7.1.5 Financial Institution Identification
7.1.5.1  ClearingSystemMemberIdentification2
Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member
of the clearing system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClearingSystemIdentification <ClrSysId> [0..1] ± 138
   MemberIdentification <MmbId> [1..1] Text 138
7.1.5.1.1  ClearingSystemIdentification <ClrSysId>
Presence: [0..1]
Definition: Specification of a pre-agreed offering between clearing agents or the channel through which
the payment instruction is processed.
ClearingSystemIdentification <ClrSysId> contains one of the following elements (see
"ClearingSystemIdentification2Choice" on page 170 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 171
Or}   Proprietary <Prtry> [1..1] Text 171
7.1.5.1.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Identification of a member of a clearing system.
Datatype: "Max35Text" on page 183
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 138 August 2026
```

