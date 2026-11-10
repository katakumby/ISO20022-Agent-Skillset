---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.4 Status <Sts>", "81.4.6.11.4.4.2 Reason <Rsn>"]
file_pages: [2796]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.4.2 Reason <Rsn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2796 to 2796.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2796

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
81.4.6.11.4.4.2  Reason <Rsn>
Presence: [0..*]
Definition: Reason for the penalty status.
Reason <Rsn> contains the following PenaltyStatusReason2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [1..1]  2796
{Or     Code <Cd> [1..1] CodeSet 2796
Or}     Proprietary <Prtry> [1..1] ± 2797
   AdditionalStatusReason <AddtlStsRsn> [0..1] Text 2797
81.4.6.11.4.4.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Provides the reason for the penalty status.
Reason <Rsn> contains one of the following PenaltyStatusReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2796
Or}   Proprietary <Prtry> [1..1] ± 2797
81.4.6.11.4.4.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Penalty status reason, in a coded form.
Datatype: "PenaltyStatusReason2Code" on page 3269
CodeName Name Definition
UPDT Updated Penalty has been updated.
SUSP TradingSuspended Penalty was removed becuase of ISIN
suspension from trading.
TECH TechnicalImpossibilities Penalty was removed becuase there
were thecnical imposssibilities at the
CSD level that prevent settlement, such
as: a failure of the infrastructure
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2796 August 2026
```

