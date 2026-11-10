---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.3 TransactionDetails <TxDtls>", "6.4.6.11.4.9.3.14 SettlementStatusFailing <SttlmStsFlng>", "6.4.6.11.4.9.3.14.2 Reason <Rsn>", "6.4.6.11.4.9.3.14.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [242]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.3.14.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 242 to 242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 242

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
6.4.6.11.4.9.3.14.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 556
6.4.6.11.4.9.3.15  BusinessDayEvent <BizDayEvt>
Presence: [0..1]
Definition: System event relevant to the computation of the penalty.
BusinessDayEvent <BizDayEvt> contains the following SystemEvent3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  242
{Or     Code <Cd> [1..1] CodeSet 242
Or}     Proprietary <Prtry> [1..1] ± 243
   ScheduledTime <SchdldTm> [1..1] DateTime 243
   EffectiveTime <FctvTm> [0..1] DateTime 243
   StartTime <StartTm> [0..1] DateTime 243
   EndTime <EndTm> [0..1] DateTime 243
6.4.6.11.4.9.3.15.1  Type <Tp>
Presence: [1..1]
Definition: Nature of the event that has occurred.
Type <Tp> contains one of the following SystemEventType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 242
Or}   Proprietary <Prtry> [1..1] ± 243
6.4.6.11.4.9.3.15.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed in a coded form.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 242 March 2026
```

