---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["2 reda.018.001.01 SecuritiesAccountCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 SecuritiesAccount <SctiesAcct>", "2.4.2.1 AccountOwner <AcctOwnr>"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 2.4.2.1 AccountOwner <AcctOwnr>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
SecuritiesAccount <SctiesAcct> contains the following SystemSecuritiesAccount7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountOwner <AcctOwnr> [1..1] ± 9
   Identification <Id> [1..1] Text 9
   Type <Tp> [1..1]  10
{Or     Code <Cd> [1..1] CodeSet 10
Or}     Proprietary <Prtry> [1..1] ± 10
   OpeningDate <OpngDt> [1..1] Date 11
   ClosingDate <ClsgDt> [0..1] Date 11
   HoldIndicator <HldInd> [1..1] Indicator 11
   NegativePosition <NegPos> [1..1] Indicator 11
   MarketSpecificAttribute <MktSpcfcAttr> [0..*]  11
     Name <Nm> [1..1] Text 12
     Value <Val> [1..1] Text 12
   Restriction <Rstrctn> [0..*]  12
     ValidFrom <VldFr> [1..1] DateTime 12
     ValidTo <VldTo> [0..1] DateTime 12
     Type <Tp> [1..1] Text 12
   EndInvestorFlag <EndInvstrFlg> [0..1] Text 13
   PricingScheme <PricgSchme> [0..1] Text 13
2.4.2.1  AccountOwner <AcctOwnr>
Presence: [1..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains the following elements (see "SystemPartyIdentification8" on
page 91 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 91
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 91
2.4.2.2  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities - Securities Account Reference Data 9 December 2019
```

