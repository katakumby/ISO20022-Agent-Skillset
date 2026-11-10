---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.13 TechnicalAttributes <TechAttrbts>"]
file_pages: [393, 394]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.13 TechnicalAttributes <TechAttrbts>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 393 to 394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 393

```text
22.1.13.2.13  TechnicalAttributes <TechAttrbts>
Presence: [0..1]
Definition: Data used for exchanges between national competent authorities, not to be used by
reporting entities.
TechnicalAttributes <TechAttrbts> contains the following RecordTechnicalData5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReceiptDateTime <RctDtTm> [1..1] DateTime 393
   ExchangeReason <XchgRsn> [1..*] CodeSet 393
22.1.13.2.13.1  ReceiptDateTime <RctDtTm>
Presence: [1..1]
Definition: Defines the date and time when the report was originally received by the national competent
authority.
Datatype: "ISODateTime" on page 449
22.1.13.2.13.2  ExchangeReason <XchgRsn>
Presence: [1..*]
Definition: Describes the reason for the exchange of the transaction report between the competent
authorities.
Datatype: "ExternalAuthorityExchangeReason1Code" on page 436
22.1.13.2.14  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C13 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
22.1.13.3  SecuritiesReferenceDataReport7
Definition: Provides details on the securities reference data for the required financial instruments.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
393 July 2025
```

## File page 394

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 395
   FinancialInstrumentGeneralAttributes
<FinInstrmGnlAttrbts>
[1..1] ± C15,
C18,
C21
395
   Issuer <Issr> [0..1] IdentifierSet 396
   TradingVenueRelatedAttributes <TradgVnRltdAttrbts> [1..*] ± C14,
C20,
C22
396
   DebtInstrumentAttributes <DebtInstrmAttrbts> [0..1]  397
     TotalIssuedNominalAmount <TtlIssdNmnlAmt> [1..1] Amount C2, C5 397
     MaturityDate <MtrtyDt> [0..1] Date 398
     NominalValuePerUnit <NmnlValPerUnit> [1..1] Amount C2, C5 398
     InterestRate <IntrstRate> [1..1] ± 398
     DebtSeniority <DebtSnrty> [0..1] CodeSet 399
   DerivativeInstrumentAttributes <DerivInstrmAttrbts> [0..1]  C9 399
     ExpiryDate <XpryDt> [0..1] Date 401
     PriceMultiplier <PricMltplr> [0..1] Quantity C6 401
     UnderlyingInstrument <UndrlygInstrm> [0..1]  401
{Or       Single <Sngl> [1..1] ± 401
Or}       Basket <Bskt> [1..1] ± C3, C10 402
     OptionType <OptnTp> [0..1] CodeSet 402
     StrikePrice <StrkPric> [0..1] ± 402
     OptionExerciseStyle <OptnExrcStyle> [0..1] CodeSet 403
     DeliveryType <DlvryTp> [0..1] CodeSet 403
     AssetClassSpecificAttributes <AsstClssSpcfcAttrbts> [0..1]  C11 404
       Commodity <Cmmdty> [0..1]  404
         Product <Pdct> [1..1] ± 405
         TransactionType <TxTp> [0..1] CodeSet 405
         FinalPriceType <FnlPricTp> [0..1] CodeSet 406
       Interest <Intrst> [0..1]  406
         InterestRate <IntrstRate> [1..1] ± 406
         FirstLegInterestRate <FrstLegIntrstRate> [0..1] ± 407
         OtherNotionalCurrency <OthrNtnlCcy> [0..1] CodeSet C2 407
         OtherLegInterestRate <OthrLegIntrstRate> [0..1] ± 407
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
394 July 2025
```

