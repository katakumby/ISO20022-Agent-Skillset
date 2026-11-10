---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.3 TransactionDetails <TxDtls>", "81.4.6.11.4.9.3.14 SettlementStatusFailing <SttlmStsFlng>", "81.4.6.11.4.9.3.14.2 Reason <Rsn>", "81.4.6.11.4.9.3.14.2.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [2824]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.3.14.2.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2824 to 2824.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2824

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
81.4.6.11.4.9.3.14.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 3327
81.4.6.11.4.9.3.15  BusinessDayEvent <BizDayEvt>
Presence: [0..1]
Definition: System event relevant to the computation of the penalty.
BusinessDayEvent <BizDayEvt> contains the following SystemEvent3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  2824
{Or     Code <Cd> [1..1] CodeSet 2824
Or}     Proprietary <Prtry> [1..1] ± 2825
   ScheduledTime <SchdldTm> [1..1] DateTime 2825
   EffectiveTime <FctvTm> [0..1] DateTime 2825
   StartTime <StartTm> [0..1] DateTime 2825
   EndTime <EndTm> [0..1] DateTime 2825
81.4.6.11.4.9.3.15.1  Type <Tp>
Presence: [1..1]
Definition: Nature of the event that has occurred.
Type <Tp> contains one of the following SystemEventType4Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2824
Or}   Proprietary <Prtry> [1..1] ± 2825
81.4.6.11.4.9.3.15.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed in a coded form.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2824 August 2026
```

