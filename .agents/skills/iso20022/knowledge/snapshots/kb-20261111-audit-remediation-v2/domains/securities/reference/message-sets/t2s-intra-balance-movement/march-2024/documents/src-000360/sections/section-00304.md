---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.3 ReportGeneralDetails <RptGnlDtls>", "16.4.3.7 UpdateType <UpdTp>"]
file_pages: [367]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.3.7 UpdateType <UpdTp>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 367 to 367.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 367

```text
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 407 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 407
Or}   Proprietary <Prtry> [1..1] ± 408
16.4.3.7  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 415 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 415
Or}   Proprietary <Prtry> [1..1] ± 415
16.4.3.8  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 495):
• Meaning When True: Yes
• Meaning When False: No
16.4.4 CashAccount <CshAcct>
Presence: [1..1]
Definition: Account to or from which a cash entry is made.
Impacted by: C12 "IdentificationOrProxyPresenceRule", C11 "IdentificationAndProxyGuideline"
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
367 March 2024
```

