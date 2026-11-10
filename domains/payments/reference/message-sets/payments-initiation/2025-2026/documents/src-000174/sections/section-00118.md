---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.8 TrackerData <TrckrData>", "3.4.3.7.8.3 TrackerRecord <TrckrRcrd>", "3.4.3.7.8.3.1 Agent <Agt>"]
file_pages: [179]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.8.3.1 Agent <Agt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 179 to 179.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 179

```text
TrackerRecord <TrckrRcrd> contains the following TrackerRecord5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Agent <Agt> [1..1] ± 179
   ChargeBearer <ChrgBr> [0..1] CodeSet 179
   ChargesAmount <ChrgsAmt> [0..1] Amount C1, C9 180
   ExchangeRateData <XchgRateData> [0..1]  180
     SourceCurrency <SrcCcy> [1..1] CodeSet C1 181
     TargetCurrency <TrgtCcy> [1..1] CodeSet C1 181
     ExchangeRate <XchgRate> [1..1] Rate 181
     UnitCurrency <UnitCcy> [0..1] CodeSet C1 181
3.4.3.7.8.3.1  Agent <Agt>
Presence: [1..1]
Definition: Identification of an agent in the tracker.
Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on
page 539 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  540
     BICFI <BICFI> [0..1] IdentifierSet C4 540
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 541
     LEI <LEI> [0..1] IdentifierSet 541
     Name <Nm> [0..1] Text 541
     PostalAddress <PstlAdr> [0..1] ± 541
     Other <Othr> [0..1] ± 542
   BranchIdentification <BrnchId> [0..1]  543
     Identification <Id> [0..1] Text 543
     LEI <LEI> [0..1] IdentifierSet 543
     Name <Nm> [0..1] Text 543
     PostalAddress <PstlAdr> [0..1] ± 543
3.4.3.7.8.3.2  ChargeBearer <ChrgBr>
Presence: [0..1]
Definition: Specifies which party/parties will bear the charges associated with the processing of the
payment transaction.
Datatype: "ChargeBearerType1Code" on page 588
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 179 March 2026
```

