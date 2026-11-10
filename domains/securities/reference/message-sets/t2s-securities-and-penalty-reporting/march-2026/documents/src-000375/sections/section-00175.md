---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.6 Penalty <Pnlty>", "6.4.6.11 PenaltyPerCounterparty <PnltyPerCtrPty>", "6.4.6.11.4 PenaltyDetails <PnltyDtls>", "6.4.6.11.4.9 RelatedTransaction <RltdTx>", "6.4.6.11.4.9.3 TransactionDetails <TxDtls>", "6.4.6.11.4.9.3.15 BusinessDayEvent <BizDayEvt>", "6.4.6.11.4.9.3.15.1 Type <Tp>", "6.4.6.11.4.9.3.15.1.2 Proprietary <Prtry>"]
file_pages: [243]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.6.11.4.9.3.15.1.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 243 to 243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 243

```text
Datatype: "ExternalSystemEventType1Code" on page 507
6.4.6.11.4.9.3.15.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of system event that has occurred, expressed as free text or a bilaterally agreed code.
.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 352
   Issuer <Issr> [0..1] Text 352
6.4.6.11.4.9.3.15.2  ScheduledTime <SchdldTm>
Presence: [1..1]
Definition: Date and time at which the event is foreseen to occur.
Datatype: "ISODateTime" on page 551
6.4.6.11.4.9.3.15.3  EffectiveTime <FctvTm>
Presence: [0..1]
Definition: Date and time at which the event effectively takes place.
Datatype: "ISODateTime" on page 551
6.4.6.11.4.9.3.15.4  StartTime <StartTm>
Presence: [0..1]
Definition: Time at which the event starts.
Datatype: "ISODateTime" on page 551
6.4.6.11.4.9.3.15.5  EndTime <EndTm>
Presence: [0..1]
Definition: Time at which the event ends.
Datatype: "ISODateTime" on page 551
6.4.6.11.4.9.4  NetMovementDetails <NetMvmntDtls>
Presence: [0..1]
Definition: Net settlement movement details for which the penalties apply.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 243 March 2026
```

