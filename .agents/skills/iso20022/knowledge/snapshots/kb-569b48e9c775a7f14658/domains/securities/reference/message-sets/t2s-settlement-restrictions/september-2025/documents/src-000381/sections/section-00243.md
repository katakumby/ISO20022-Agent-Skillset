---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.21 Status", "9.1.21.19 MatchingDenied3Choice"]
file_pages: [289]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.21.19 MatchingDenied3Choice

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 289 to 289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 289

```text
9.1.21.19  MatchingDenied3Choice
Definition: Specifies the matching processing change requested.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 289
Or}   Proprietary <Prtry> [1..1] ± 289
9.1.21.19.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the execution of a matching denial process.
Datatype: "MatchingProcess1Code" on page 330
CodeName Name Definition
UNMT Unmatch The referenced transaction is requested
to be unmatched.
MTRE ResumeMatching Matching process is to be resumed for
the referenced transaction.
9.1.21.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the execution of a matching denial process.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.21.20  SecuritiesPaymentStatus5Choice
Definition: Choice of format for the status of payment of a security at a particular time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 289
Or}   Proprietary <Prtry> [1..1] ± 290
9.1.21.20.1  Code <Cd>
Presence: [1..1]
Definition: Securities payment status expressed as an ISO 20022 code.
Datatype: "SecuritiesPaymentStatus1Code" on page 338
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 289 September 2025
```

