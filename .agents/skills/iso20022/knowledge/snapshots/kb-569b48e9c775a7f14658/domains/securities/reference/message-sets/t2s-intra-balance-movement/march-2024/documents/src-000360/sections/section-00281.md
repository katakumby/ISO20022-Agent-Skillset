---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.3 ReportGeneralDetails <RptGnlDtls>", "15.4.3.8 ActivityIndicator <ActvtyInd>"]
file_pages: [340]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.3.8 ActivityIndicator <ActvtyInd>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 340 to 340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 340

```text
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 415 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 415
Or}   Proprietary <Prtry> [1..1] ± 415
15.4.3.8  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 495):
• Meaning When True: Yes
• Meaning When False: No
15.4.4 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C11 "IdentificationOrProxyPresenceRule", C10 "IdentificationAndProxyGuideline"
CashAccount <CshAcct> contains the following elements (see "CashAccount40" on page 387 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 388
   Type <Tp> [0..1] ± 388
   Currency <Ccy> [0..1] CodeSet C2 388
   Name <Nm> [0..1] Text 389
   Proxy <Prxy> [0..1] ± 389
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
340 March 2024
```

