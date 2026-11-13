---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.4 Status <Sts>", "6.4.6.11.4.4.2 Reason <Rsn>"]
file_pages: [214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.4.2 Reason <Rsn>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 214 to 214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 214

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
6.4.6.11.4.4.2  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the penalty status.
Reason <Rsn> contains the following PenaltyStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  214
{Or     Code <Cd> [1..1] CodeSet 214
Or}     Proprietary <Prtry> [1..1] ± 215
   AdditionalStatusReason <AddtlStsRsn> [0..1] Text 215
6.4.6.11.4.4.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Provides the reason for the penalty status.
Reason <Rsn> contains one of the following PenaltyStatusReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 214
Or}   Proprietary <Prtry> [1..1] ± 215
6.4.6.11.4.4.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Penalty status reason, in a coded form.
Datatype: "PenaltyStatusReason2Code" on page 518
CodeName Name Definition
UPDT Updated Penalty has been updated.
SUSP TradingSuspended Penalty was removed becuase of ISIN
suspension from trading.
TECH TechnicalImpossibilities Penalty was removed becuase there
were thecnical imposssibilities at the
CSD level that prevent settlement, such
as: a failure of the infrastructure
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 214 March 2026
```

