---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["30 camt.069.001.05 GetStandingOrderV05", "30.4 Message Building Blocks", "30.4.2 StandingOrderQueryDefinition <StgOrdrQryDef>", "30.4.2.2 StandingOrderCriteria <StgOrdrCrit>", "30.4.2.2.2 NewCriteria <NewCrit>", "30.4.2.2.2.2 SearchCriteria <SchCrit>", "30.4.2.2.2.2.3 Type <Tp>"]
file_pages: [697]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.069.001.05"]
---

# 30.4.2.2.2.2.3 Type <Tp>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 697 to 697.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 697

```text
30.4.2.2.2.2.3  Type <Tp>
Presence: [0..1]
Definition: Type of the standing order.
Type <Tp> contains one of the following StandingOrderType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 697
Or}   Proprietary <Prtry> [1..1] ± 697
30.4.2.2.2.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Liquidity transfer standing order type, in a coded form.
Datatype: "StandingOrderType1Code" on page 873
CodeName Name Definition
USTO UserDefinedStandingOrder Liquidity transfer standing order type,
that has been customised or defined to
the specific need of the user.
PSTO PredefinedStandingOrder Liquidity transfer standing order type, as
predefined in the system.
30.4.2.2.2.2.3.2  Proprietary <Prtry>
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
30.4.2.2.2.2.4  Account <Acct>
Presence: [0..1]
Definition: Liquidity transfer origin or destination account within the pool of accounts under management
of the requestor.
Impacted by: C7 "IdentificationOrProxyPresenceRule", C6 "IdentificationAndProxyGuideline"
Approved by the Payments SEG on 04 February 2025 camt.069.001.05 GetStandingOrderV05
Cash Management - Maintenance 2024 - 2025 697 February 2025
```

