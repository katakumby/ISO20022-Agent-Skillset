---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.13 Regulatory Reporting", "22.1.13.2 SecuritiesTransactionReport7", "22.1.13.2.9 FinancialInstrument <FinInstrm>", "22.1.13.2.9.3 Other <Othr>", "22.1.13.2.9.3.1 FinancialInstrumentGeneralAttributes <FinInstrmGnlAttrbts>", "22.1.13.2.9.3.1.2 OtherIdentification <OthrId>", "22.1.13.2.9.3.1.2.3 Type <Tp>"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.13.2.9.3.1.2.3 Type <Tp>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
22.1.13.2.9.3.1.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 333 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 333
Or}   Proprietary <Prtry> [1..1] Text 333
22.1.13.2.9.3.1.3  FullName <FullNm>
Presence: [1..1]
Definition: Full name or description of the financial instrument.
Datatype: "Max350Text" on page 455
22.1.13.2.9.3.1.4  ClassificationType <ClssfctnTp>
Presence: [1..1]
Definition: Classification type of the financial instrument, as per the ISO classification of financial
instrument (CFI) codification, that is common share with voting rights, fully paid, or registered.
Datatype: "CFIOct2015Identifier" on page 450
22.1.13.2.9.3.1.5  NotionalCurrency <NtnlCcy>
Presence: [0..1]
Definition: Currency in which the notional is denominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.13.2.9.3.2  DebtInstrumentAttributes <DebtInstrmAttrbts>
Presence: [0..1]
Definition: Attributes specific to debt instruments.
DebtInstrumentAttributes <DebtInstrmAttrbts> contains the following elements (see
"DebtInstrument4" on page 414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MaturityDate <MtrtyDt> [1..1] Date 414
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
382 July 2025
```

