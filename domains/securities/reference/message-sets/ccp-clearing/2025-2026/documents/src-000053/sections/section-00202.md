---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.4 Message Building Blocks", "8.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>", "8.4.4.5 SafekeepingPlace <SfkpgPlc>", "8.4.4.5.1 Identification <Id>"]
file_pages: [264]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.4.4.5.1 Identification <Id>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 264 to 264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 264

```text
SafekeepingPlace <SfkpgPlc> contains one of the following SafekeepingPlaceFormat7Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  264
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 264
     Identification <Id> [0..1] Text 264
Or   Country <Ctry> [1..1] CodeSet   'C6 265
Or   TypeAndIdentification <TpAndId> [1..1]  265
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 265
     Identification <Id> [1..1] IdentifierSet   'C4 266
Or}   Proprietary <Prtry> [1..1]  266
     Identification <Id> [0..1] Text 266
     Type <Tp> [1..1]  267
       Identification <Id> [1..1] Text 267
       Issuer <Issr> [1..1] Text 267
       SchemeName <SchmeNm> [0..1] Text 267
8.4.4.5.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 264
   Identification <Id> [0..1] Text 264
8.4.4.5.1.1  SafekeepingPlaceType <SfkpgPlcTp>
Presence: [1..1]
Definition: Place of safekeeping as a code.
Datatype: SafekeepingPlace3Code on page 482
CodeName Name Definition
SHHE SharesHeldElsewhere Used for certain financial instruments, for
example, US mutual funds, where
settlement is internal only, that is, there
is no external movement of securities.
8.4.4.5.1.2  Identification <Id>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 264
```

