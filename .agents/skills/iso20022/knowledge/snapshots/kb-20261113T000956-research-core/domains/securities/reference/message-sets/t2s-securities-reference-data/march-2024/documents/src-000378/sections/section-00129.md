---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.2 Derivative4", "13.1.2.2.2 Option <Optn>", "13.1.2.2.2.16 AdditionalUnderlyingAttributes <AddtlUndrlygAttrbts>", "13.1.2.2.2.16.3 SettlementType <SttlmTp>", "13.1.2.2.2.16.3.1 Code <Cd>"]
file_pages: [188]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.2.2.16.3.1 Code <Cd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 188 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
SettlementType <SttlmTp> contains one of the following SettlementType3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 188
Or}   Proprietary <Prtry> [1..1] ± 188
13.1.2.2.2.16.3.1  Code <Cd>
Presence: [1..1]
Definition: Settlement type expressed as an ISO 20022 code.
Datatype: "SettlementType1Code" on page 523
CodeName Name Definition
PRIN Principal Option trade is settled as principal.
NETO NettedOff Option trade is netted off against another
trade.
13.1.2.2.2.16.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 478 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 479
   Issuer <Issr> [1..1] Text 479
   SchemeName <SchmeNm> [0..1] Text 479
13.1.2.2.2.16.4  CashAmount <CshAmt>
Presence: [0..1]
Definition: Cash amount associated with the underlying component. Necessary for derivatives that
deliver into more than one underlying instrument and one of the underlying's is a fixed cash value.
Impacted by: C1 "ActiveCurrency", C5 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 506
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 188 March 2024
```

