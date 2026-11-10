---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.18 AgreedRate <AgrdRate>", "4.4.3.18.2 QuotedCurrency <QtdCcy>"]
file_pages: [315]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.18.2 QuotedCurrency <QtdCcy>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 315 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 315

```text
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 1224
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
4.4.3.18.2  QuotedCurrency <QtdCcy>
Presence: [0..1]
Definition: Currency into which the base (unit) currency is converted. In the example GBP 1.00 = USD
1.30, the unit currency is USD.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 1224
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
4.4.3.18.3  PreAgreedExchangeRate <PreAgrdXchgRate>
Presence: [1..1]
Definition: The value of one currency expressed in relation to another currency. ExchangeRate
expresses the ratio between UnitCurrency and QuotedCurrency. (Amount in UnitCurrency *
ExchangeRate = Amount in QuotedCurrency)
Datatype: "BaseOneRate" on page 1242
4.4.3.18.4  QuotationDateTime <QtnDtTm>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 1239
4.4.3.18.5  QuoteIdentification <QtId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the quote issued by the
ForeignExchangeAgent.
Usage: This identification must be passed on throughout the entire end-to-end chain.
Datatype: "UUIDv4Identifier" on page 1241
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
315 March 2026
```

