---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.8 Transaction <Tx>", "22.1.13.2.8.9 CountryOfBranch <CtryOfBrnch>"]
file_pages: [375]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.8.9 CountryOfBranch <CtryOfBrnch>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 375 to 375.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 375

```text
Use the ISO 10383 segment MIC (4 characters) for financial instruments executed on a MiFID trading
venue, System Internaliser (SI) or non-EU organised trading platform. Where the segment MIC does
not exist, use the operating MIC.
Use MIC code 'XOFF' for financial instruments admitted to trading or traded on a trading venue, where
the transaction on that financial instrument is not executed on a MiFID trading venue, SI or non-EU
organised trading platform, or where an investment firm does not know it is trading with another
investment firm acting as an SI.
Use MIC code 'XXXX' for financial instruments that are not admitted to trading or traded on a trading
venue or for which no request for admission has been made and that are not traded on an non-EU
organised trading platform but where the underlying is admitted to trading or traded on a trading venue.
Datatype: "MICIdentifier" on page 451
22.1.13.2.8.9  CountryOfBranch <CtryOfBrnch>
Presence: [0..1]
Definition: Country of the branch of the investment firm whose market membership was used to execute
the transaction.
TBC with item 46.
Impacted by: C4 "Country"
Datatype: "CountryCode" on page 434
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
22.1.13.2.8.10  UpFrontPayment <UpFrntPmt>
Presence: [0..1]
Definition: Monetary value of any up-front payment in basis points of notional received or paid by the
seller.
Where the seller receives the up-front payment, the value populated is positive. Where the seller pays
the up-front payment, the value populated is negative.
For increase or decrease in notional derivative contracts, the number shall reflect the absolute value of
the change and shall be expressed as a positive number.
UpFrontPayment <UpFrntPmt> contains the following elements (see "AmountAndDirection53" on
page 274 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C5 274
   Sign <Sgn> [0..1] Indicator 274
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
375 July 2025
```

