---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.4 Status <Sts>", "6.4.6.11.4.4.1 Status <Sts>"]
file_pages: [213]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.4.1 Status <Sts>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 213 to 213.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 213

```text
Definition: Status of a penalty.
Status <Sts> contains the following PenaltyStatus2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1]  213
{Or     Code <Cd> [1..1] CodeSet 213
Or}     Proprietary <Prtry> [1..1] ± 213
   Reason <Rsn> [0..*]  214
     Reason <Rsn> [1..1]  214
{Or       Code <Cd> [1..1] CodeSet 214
Or}       Proprietary <Prtry> [1..1] ± 215
     AdditionalStatusReason <AddtlStsRsn> [0..1] Text 215
6.4.6.11.4.4.1  Status <Sts>
Presence: [1..1]
Definition: Status of a penalty.
Status <Sts> contains one of the following PenaltyStatus2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 213
Or}   Proprietary <Prtry> [1..1] ± 213
6.4.6.11.4.4.1.1  Code <Cd>
Presence: [1..1]
Definition: Penalty status, , in a coded form.
Datatype: "PenaltyStatus2Code" on page 518
CodeName Name Definition
ACTV Active Penalty is active for the party.
NCOM NotComputed Penalty could not be computed.
REMO Removed Removal of a cash penalty where
settlement cannot be performed for
reasons that are independent from any
of the CSD participants or the CSD.
6.4.6.11.4.4.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Penalty status, in a proprietary form.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 213 March 2026
```

