---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.6 Penalty <Pnlty>", "81.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "81.4.6.11.4 PenaltyDetails <PnltyDtls>", "81.4.6.11.4.9 RelatedTransaction <RltdTx>", "81.4.6.11.4.9.3 TransactionDetails <TxDtls>", "81.4.6.11.4.9.3.15 BusinessDayEvent <BizDayEvt>", "81.4.6.11.4.9.3.15.1 Type <Tp>", "81.4.6.11.4.9.3.15.1.2 Proprietary <Prtry>"]
file_pages: [2825]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.6.11.4.9.3.15.1.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2825 to 2825.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2825

```text
Datatype: "ExternalSystemEventType1Code" on page 3246
81.4.6.11.4.9.3.15.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed as free text or a bilaterally agreed code.
.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
81.4.6.11.4.9.3.15.2  ScheduledTime <SchdldTm>
Presence: [1..1]
Definition: Date and time at which the event is foreseen to occur.
Datatype: "ISODateTime" on page 3320
81.4.6.11.4.9.3.15.3  EffectiveTime <FctvTm>
Presence: [0..1]
Definition: Date and time at which the event effectively takes place.
Datatype: "ISODateTime" on page 3320
81.4.6.11.4.9.3.15.4  StartTime <StartTm>
Presence: [0..1]
Definition: Time at which the event starts.
Datatype: "ISODateTime" on page 3320
81.4.6.11.4.9.3.15.5  EndTime <EndTm>
Presence: [0..1]
Definition: Time at which the event ends.
Datatype: "ISODateTime" on page 3320
81.4.6.11.4.9.4  NetMovementDetails <NetMvmntDtls>
Presence: [0..1]
Definition: Net settlement movement details for which the penalties apply.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2825 August 2026
```

