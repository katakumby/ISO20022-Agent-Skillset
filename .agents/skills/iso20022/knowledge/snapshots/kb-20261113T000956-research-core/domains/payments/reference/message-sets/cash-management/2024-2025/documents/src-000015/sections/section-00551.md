---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["31 camt.070.001.06 ReturnStandingOrderV06", "31.4 Message Building Blocks", "31.4.2 ReportOrError <RptOrErr>", "31.4.2.1 Report <Rpt>", "31.4.2.1.2 StandingOrderOrError <StgOrdrOrErr>", "31.4.2.1.2.1 StandingOrder <StgOrdr>", "31.4.2.1.2.1.4 Type <Tp>"]
file_pages: [723]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.070.001.06"]
---

# 31.4.2.1.2.1.4 Type <Tp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 723 to 723.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 723

```text
Definition: Unique and unambiguous identification for a standing order, as assigned by the account
servicer or the account owner.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 849
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
31.4.2.1.2.1.4  Type <Tp>
Presence: [0..1]
Definition: Type of the standing order.
Type <Tp> contains one of the following StandingOrderType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 723
Or}   Proprietary <Prtry> [1..1] ± 723
31.4.2.1.2.1.4.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer standing order type, in a coded form.
Datatype: "StandingOrderType1Code" on page 873
CodeName Name Definition
USTO UserDefinedStandingOrder Liquidity transfer standing order type,
that has been customised or defined to
the specific need of the user.
PSTO PredefinedStandingOrder Liquidity transfer standing order type, as
predefined in the system.
31.4.2.1.2.1.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Liquidity transfer standing order type, in a free text form.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 809 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 809
   SchemeName <SchmeNm> [0..1] Text 809
   Issuer <Issr> [0..1] Text 809
Approved by the Payments SEG on 04 February 2025 camt.070.001.06 ReturnStandingOrderV06
Cash Management - Maintenance 2024 - 2025 723 February 2025
```

