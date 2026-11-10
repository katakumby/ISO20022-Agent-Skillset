---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.7 ChargesInformation <ChrgsInf>", "3.4.3.7.7.3 Type <Tp>", "3.4.3.7.7.3.1 Code <Cd>"]
file_pages: [177]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.7.3.1 Code <Cd>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 177 to 177.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 177

```text
Type <Tp> contains one of the following ChargeType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 177
Or}   Proprietary <Prtry> [1..1] ± 177
3.4.3.7.7.3.1  Code <Cd>
Presence: [1..1]
Definition: Charge type, in a coded form.
Datatype: "ExternalChargeType1Code" on page 592
3.4.3.7.7.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of charge in a proprietary form, as defined by the issuer.
Proprietary <Prtry> contains the following elements (see "GenericIdentification3" on page 548 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 548
   Issuer <Issr> [0..1] Text 548
3.4.3.7.8  TrackerData <TrckrData>
Presence: [0..1]
Definition: Provides information on the tracking of the interbank transaction related to the payment.
TrackerData <TrckrData> contains the following TrackerData7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConfirmedDate <ConfdDt> [1..1] ± 178
   ConfirmedAmount <ConfdAmt> [1..1] Amount C1, C9 178
   TrackerRecord <TrckrRcrd> [1..*]  178
     Agent <Agt> [1..1] ± 179
     ChargeBearer <ChrgBr> [0..1] CodeSet 179
     ChargesAmount <ChrgsAmt> [0..1] Amount C1, C9 180
     ExchangeRateData <XchgRateData> [0..1]  180
       SourceCurrency <SrcCcy> [1..1] CodeSet C1 181
       TargetCurrency <TrgtCcy> [1..1] CodeSet C1 181
       ExchangeRate <XchgRate> [1..1] Rate 181
       UnitCurrency <UnitCcy> [0..1] CodeSet C1 181
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 177 March 2026
```

