---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.3 TransactionInformationAndStatus <TxInfAndSts>", "2.4.3.9 ChargesInformation <ChrgsInf>", "2.4.3.9.3 Type <Tp>", "2.4.3.9.3.1 Code <Cd>"]
file_pages: [39]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.002.001.16"]
---

# 2.4.3.9.3.1 Code <Cd>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 39 to 39.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
Type <Tp> contains one of the following ChargeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 39
Or}   Proprietary <Prtry> [1..1] ± 39
2.4.3.9.3.1  Code <Cd>
Presence: [1..1]
Definition: Charge type, in a coded form.
Datatype: "ExternalChargeType1Code" on page 1228
2.4.3.9.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of charge in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 1184 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1185
   Issuer <Issr> [0..1] Text 1185
2.4.3.10  AcceptanceDateTime <AccptncDtTm>
Presence: [0..1]
Definition: Point in time when the payment order from the initiating party meets the processing
conditions of the account servicing agent. This means that the account servicing agent has received the
payment order and has applied checks such as authorisation, availability of funds.
Datatype: "ISODateTime" on page 1239
2.4.3.11  ProcessingDate <PrcgDt>
Presence: [0..1]
Definition: Date/time at which the instruction was processed by the specified party.
ProcessingDate <PrcgDt> contains one of the following elements (see "DateAndDateTime2Choice"
on page 1168 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1169
Or}   DateTime <DtTm> [1..1] DateTime 1169
2.4.3.12  EffectiveInterbankSettlementDate <FctvIntrBkSttlmDt>
Presence: [0..1]
Definition: Date and time at which a transaction is completed and cleared, that is, payment is effected.
Approved by the Payments SEG on 12 January 2026 pacs.002.001.16 FIToFIPaymentStatusReportV16
Payments Clearing and Settlement - Maintenance 2025 -
2026
39 March 2026
```

