---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.4 Message Building Blocks", "8.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>", "8.4.4.5 SafekeepingPlace <SfkpgPlc>", "8.4.4.5.4 Proprietary <Prtry>", "8.4.4.5.4.2 Type <Tp>"]
file_pages: [267]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.4.4.5.4.2 Type <Tp>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 267 to 267.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 267

```text
8.4.4.5.4.2  Type <Tp>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Type <Tp> contains the following GenericIdentification40 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 267
   Issuer <Issr> [1..1] Text 267
   SchemeName <SchmeNm> [0..1] Text 267
8.4.4.5.4.2.1  Identification <Id>
Presence: [1..1]
Definition: Proprietary information, often a code, issued by the data source scheme issuer.
Datatype: Exact4AlphaNumericText on page 492
8.4.4.5.4.2.2  Issuer <Issr>
Presence: [1..1]
Definition: Entity that assigns the identification.
Datatype: Max35Text on page 493
8.4.4.5.4.2.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: Max35Text on page 493
8.4.4.6  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Clearing member account at the central securities depository.
SafekeepingAccount <SfkpgAcct> contains the following elements (see SecuritiesAccount19 on
page 375 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 375
   Type <Tp> [0..1] ± 375
   Name <Nm> [0..1] Text 375
8.4.4.7  ClearingSegment <ClrSgmt>
Presence: [0..1]
Definition: Clearing organisation that will clear the trade.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 267
```

