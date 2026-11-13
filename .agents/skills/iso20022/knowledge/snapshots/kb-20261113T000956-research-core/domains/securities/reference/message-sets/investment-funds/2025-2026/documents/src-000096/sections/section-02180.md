---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.12 ForeignExchangeDetails <FXDtls>", "50.4.4.9.12.4 QuotationDate <QtnDt>"]
file_pages: [3069]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.12.4 QuotationDate <QtnDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3069 to 3069.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3069

```text
1 x CUR1 = nnn x CUR2,
where:
CUR1 is the unit currency
CUR2 is the quoted currency
nnn is the exchange rate.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Datatype: "BaseOneRate" on page 5401
50.4.4.9.12.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 5388
50.4.4.9.12.5  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes a foreign exchange rate.
QuotingInstitution <QtgInstn> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
50.4.4.9.13  IncomePreference <IncmPref>
Presence: [0..1]
Definition: Dividend option chosen by the account owner based on the options offered in the
prospectus.
Datatype: "IncomePreference1Code" on page 5310
CodeName Name Definition
CASH Cash Distribution in cash.
DRIP DividendReinvestment Reinvestment of proceeds into
securities.
50.4.4.9.14  LetterIntentReference <LttrInttRef>
Presence: [0..1]
Definition: Reference of a letter of intent program, in which sales commissions are reduced based on
the aggregate of a customer's actual purchase and anticipated purchases, over a specific period of
time, and as agreed by the customer. A letter of intent program is mainly used in the US market.
Datatype: "Max35Text" on page 5403
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3069 May 2026
```

