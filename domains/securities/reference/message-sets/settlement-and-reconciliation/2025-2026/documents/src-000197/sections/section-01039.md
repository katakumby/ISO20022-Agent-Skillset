---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.12 Foreign Exchange", "35.1.12.1 ForeignExchangeTerms34", "35.1.12.1.4 QuotationDate <QtnDt>"]
file_pages: [1478]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.12.1.4 QuotationDate <QtnDt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1478 to 1478.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1478

```text
Definition: The value of one currency expressed in relation to another currency. ExchangeRate
expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/
QuotedCurrency).
Datatype: "BaseOneRate" on page 2189
35.1.12.1.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 2185
35.1.12.1.5  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes a foreign exchange rate.
QuotingInstitution <QtgInstn> contains one of the following elements (see
"PartyIdentification120Choice" on page 1689 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1689
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1689
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1690
35.1.13 Frequency
35.1.13.1  Frequency25Choice
Definition: Choice of format for a frequency, for example, the frequency of delivery of a statement.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1478
Or}   Proprietary <Prtry> [1..1] ± 1479
35.1.13.1.1  Code <Cd>
Presence: [1..1]
Definition: Frequency expressed as an ISO 20022 code.
Datatype: "EventFrequency4Code" on page 2062
CodeName Name Definition
YEAR Annual Event takes place every year or once a
year.
ADHO Adhoc Event takes place as necessary.
MNTH Monthly Event takes place every month or once a
month.
DAIL Daily Event takes place every day.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1478 March 2026
```

