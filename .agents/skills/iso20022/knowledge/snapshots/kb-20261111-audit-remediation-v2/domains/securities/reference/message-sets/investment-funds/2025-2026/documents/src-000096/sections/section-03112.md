---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.8 AccountIdentificationFormatChoice", "66.1.2.8.2 IdentificationAndPurpose <IdAndPurp>", "66.1.2.8.2.1 Identification <Id>"]
file_pages: [4336]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.8.2.1 Identification <Id>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4336 to 4336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4336

```text
IdentificationAndPurpose <IdAndPurp> contains the following AccountIdentificationAndPurpose
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4336
   Purpose <Purp> [1..1] CodeSet 4336
66.1.2.8.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains the following elements (see "AccountIdentification1" on page 4328 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Proprietary <Prtry> [1..1] ± 4329
66.1.2.8.2.2  Purpose <Purp>
Presence: [1..1]
Definition: Specifies the purpose of the account.
Datatype: "SecuritiesAccountPurposeType1Code" on page 5359
CodeName Name Definition
MARG Margin Account is used when financing is done
by the broker.
SHOR ShortSale Account is used for short sale orders.
ABRD Abroad Account is located in a financial
institution outside the country where the
transaction is taking place.
CEND Centralised Account and all its related positions are
held in one location.
DVPA CashDVP Account is used for settlement upon
delivery, or a collection on a delivery
basis.
PHYS Physical Account is used for physical domestic
safekeeping.
66.1.2.8.3  IdentificationAsDSS <IdAsDSS>
Presence: [1..1]
Definition: Identification of the account expressed with a data source scheme, a code used within the
data source scheme and the account identification.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4336 May 2026
```

