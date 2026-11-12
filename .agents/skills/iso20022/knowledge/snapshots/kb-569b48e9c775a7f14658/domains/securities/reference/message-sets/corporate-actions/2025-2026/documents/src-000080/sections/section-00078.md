---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.23 ChangeType <ChngTp>"]
file_pages: [124]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.23 ChangeType <ChngTp>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 124 to 124.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 124

```text
AdditionalBusinessProcessIndicator <AddtlBizPrcInd> contains one of the following elements (see
"AdditionalBusinessProcessFormat17Choice" on page 889 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 889
Or}   Proprietary <Prtry> [1..1] ± 891
3.4.10.23  ChangeType <ChngTp>
Presence: [0..*]
Definition: Specifies the type of change announced.
ChangeType <ChngTp> contains one of the following elements (see
"CorporateActionChangeTypeFormat5Choice" on page 948 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 948
Or}   Proprietary <Prtry> [1..1] ± 948
3.4.10.24  FollowingEventTypeIndicator <FllwngEvtTpInd>
Presence: [0..1]
Definition: Specifies the event type of the following event.
FollowingEventTypeIndicator <FllwngEvtTpInd> contains one of the following elements (see
"IntermediateSecuritiesDistributionTypeFormat19Choice" on page 986 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 986
Or}   Proprietary <Prtry> [1..1] ± 987
3.4.10.25  CapitalGainInOutIndicator <CptlGnInOutInd>
Presence: [0..1]
Definition: Specifies whether the capital gain is in the scope of the EU Savings directive for the income
realised upon the sale, refund or redemption of shares and units (.) (Article 6(1d)).
CapitalGainInOutIndicator <CptlGnInOutInd> contains one of the following elements (see
"CapitalGainFormat3Choice" on page 905 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 905
Or}   Proprietary <Prtry> [1..1] ± 905
3.4.10.26  TaxableIncomePerShareCalculated <TaxblIncmPerShrClctd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 124 February 2026
```

