---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.21 Foreign Exchange", "66.1.21.3 ForeignExchangeTerms37", "66.1.21.3.5 ExchangeRate <XchgRate>"]
file_pages: [4534]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.21.3.5 ExchangeRate <XchgRate>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4534 to 4534.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4534

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.21.3.5  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects
that amount of the quoted currency that can be purchased with one unit of the unit currency, as follows:
1 x CUR1 = nnn x CUR2,
where:
CUR1 is the unit currency
CUR2 is the quoted currency
nnn is the exchange rate.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Datatype: "BaseOneRate" on page 5401
66.1.21.3.6  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 5388
66.1.21.3.7  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes the foreign exchange rate.
QuotingInstitution <QtgInstn> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.22 Frequency
66.1.22.1  StatementFrequencyReason2Choice
Definition: Choice of formats for the specification of the statement frequency.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4535
Or}   Proprietary <Prtry> [1..1] ± 4535
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4534 May 2026
```

