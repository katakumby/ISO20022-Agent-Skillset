---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.42 RedemptionType <RedTp>", "27.4.2.3.42.2 Proprietary <Prtry>"]
file_pages: [791]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.42.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 791 to 791.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 791

```text
CodeName Name Definition
PRNR PartialRedemptionWithoutReduction Indicates that the type of redemption at
maturity is partial without reduction.
PRWR PartialRedemptionWithReduction Indicates that the type of redemption at
maturity is partial with reduction.
RNDM DrawingAtRandom Indicates that the type of redemption at
maturity is drawing at random.
PRRA DrawingProRata Indicates that the type of redemption at
maturity is drawing pro-rata.
CALL Call Indicates that the type of redemption at
maturity is call.
PUUT Put Indicates that the type of redemption at
maturity is put.
27.4.2.3.42.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Maturity redemption type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
27.4.2.3.43  RedemptionPaymentCurrency <RedPmtCcy>
Presence: [0..1]
Definition: ISO currency for the payment of the cash proceeds.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
27.4.2.3.44  Restriction <Rstrctn>
Presence: [0..*]
Definition: Regulatory restriction(s) linked to the security.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 791 August 2026
```

