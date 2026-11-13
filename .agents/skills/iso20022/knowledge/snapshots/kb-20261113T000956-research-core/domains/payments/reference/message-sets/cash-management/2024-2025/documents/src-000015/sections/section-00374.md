---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["16 camt.017.001.05 ReturnCurrencyExchangeRateV05", "16.4 Message Building Blocks", "16.4.2 ReportOrError <RptOrErr>", "16.4.2.1 CurrencyExchangeReport <CcyXchgRpt>", "16.4.2.1.2 CurrencyExchangeOrError <CcyXchgOrErr>", "16.4.2.1.2.2 CurrencyExchange <CcyXchg>", "16.4.2.1.2.2.5 HighLimit <HghLmt>", "16.4.2.1.2.2.5.1 Rate <Rate>"]
file_pages: [520, 521]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.017.001.05"]
---

# 16.4.2.1.2.2.5.1 Rate <Rate>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 520 to 521.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 520

```text
Usage: The currency authority publishes the exchange rate based on the price formed in the foreign
exchange market, allowing it to float up and down within the prescribed fluctuation range. It is the
highest exchange rate supported in foreign exchange market transactions.
HighLimit <HghLmt> contains one of the following ExchangeRateOrPercentage1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 520
Or}   Percentage <Pctg> [1..1] Rate 520
16.4.2.1.2.2.5.1  Rate <Rate>
Presence: [1..1]
Definition: Rate is expressed an currency exchange rate.
Datatype: "BaseOneRate" on page 886
16.4.2.1.2.2.5.2  Percentage <Pctg>
Presence: [1..1]
Definition: Rate is expressed as a percentage relative to the reference rate.
Datatype: "PercentageRate" on page 887
16.4.2.2  OperationalError <OprlErr>
Presence: [1..*]
Definition: Indicates that an operational error has been issued during the processing of the related
request.
OperationalError <OprlErr> contains the following elements (see "ErrorHandling3" on page 816 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Error <Err> [1..1]  816
{Or     Code <Cd> [1..1] CodeSet 817
Or}     Proprietary <Prtry> [1..1] Text 817
   Description <Desc> [0..1] Text 817
16.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C2 "SupplementaryDataRule"
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 520 February 2025
```

## File page 521

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.017.001.05 ReturnCurrencyExchangeRateV05
Cash Management - Maintenance 2024 - 2025 521 February 2025
```

