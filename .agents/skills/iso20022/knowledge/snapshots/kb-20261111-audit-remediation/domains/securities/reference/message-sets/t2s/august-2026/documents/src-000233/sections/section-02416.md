---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.32 Transaction Type", "82.1.32.2 TradeTransactionCondition5Choice", "82.1.32.2.2 Proprietary <Prtry>"]
file_pages: [3207]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.32.2.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3207 to 3207.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3207

```text
CodeName Name Definition
BCRO ResultOption Result of option when set. (UK specific).
BCRP ResultRepo Result of repo when set (UK specific).
BCFD DeliveryForm Form of delivery, not for foreign
registration when unset (UK specific).
BCBL BoardLot Board lots, not set for odd lots (UK
specific).
BCBN BadName Bad names, not set for good names (UK
specific).
MAPR MarketPrice Trade was executed at market price.
NEGO NegotiatedTrade Trade for which the price is not the one
quoted but an improved one, that is, the
negotiated price.
NMPR NonMarketPrice Trade was executed outside of normal
market conditions, for example, in the
case of an iceberg order.
BCPD DeliverCountryIncorporation Place of delivery, in country of
incorporation when unset (UK specific).
82.1.32.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade conditions expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.32.3  TransactionActivity3Choice
Definition: Choice of format for the transaction activity identification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3207
Or}   Proprietary <Prtry> [1..1] ± 3208
82.1.32.3.1  Code <Cd>
Presence: [1..1]
Definition: Transaction type expressed as an ISO 20022 code.
Datatype: "TransactionActivity1Code" on page 3311
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3207 August 2026
```

