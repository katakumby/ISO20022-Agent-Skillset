---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["38 reda.018.001.01 SecuritiesAccountCreationRequestV01", "38.4 Message Building Blocks", "38.4.2 SecuritiesAccount <SctiesAcct>", "38.4.2.1 AccountOwner <AcctOwnr>"]
file_pages: [2101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 38.4.2.1 AccountOwner <AcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2101 to 2101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2101

```text
SecuritiesAccount <SctiesAcct> contains the following SystemSecuritiesAccount7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [1..1] ± 2101
   Identification <Id> [1..1] Text 2101
   Type <Tp> [1..1]  2102
{Or     Code <Cd> [1..1] CodeSet 2102
Or}     Proprietary <Prtry> [1..1] ± 2102
   OpeningDate <OpngDt> [1..1] Date 2103
   ClosingDate <ClsgDt> [0..1] Date 2103
   HoldIndicator <HldInd> [1..1] Indicator 2103
   NegativePosition <NegPos> [1..1] Indicator 2103
   MarketSpecificAttribute <MktSpcfcAttr> [0..*]  2103
     Name <Nm> [1..1] Text 2104
     Value <Val> [1..1] Text 2104
   Restriction <Rstrctn> [0..*]  2104
     ValidFrom <VldFr> [1..1] DateTime 2104
     ValidTo <VldTo> [0..1] DateTime 2104
     Type <Tp> [1..1] Text 2104
   EndInvestorFlag <EndInvstrFlg> [0..1] Text 2105
   PricingScheme <PricgSchme> [0..1] Text 2105
38.4.2.1  AccountOwner <AcctOwnr>
Presence: [1..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
38.4.2.2  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities 2101 August 2026
```

