---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.2 RequestedModification <ReqdMod>", "6.4.3.2.1 SystemSecuritiesAccount <SysSctiesAcct>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 6.4.3.2.1 SystemSecuritiesAccount <SysSctiesAcct>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
RequestedModification <ReqdMod> contains one of the following
SecuritiesAccountModification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SystemSecuritiesAccount <SysSctiesAcct> [1..1]  52
     ClosingDate <ClsgDt> [0..1] Date 52
     HoldIndicator <HldInd> [0..1] Indicator 52
     NegativePosition <NegPos> [0..1] Indicator 53
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 53
     PricingScheme <PricgSchme> [0..1] Text 53
Or   SystemRestriction <SysRstrctn> [1..1]  53
     ValidFrom <VldFr> [1..1] DateTime 53
     ValidTo <VldTo> [0..1] DateTime 54
     Type <Tp> [1..1] Text 54
Or}   MarketSpecificAttribute <MktSpcfcAttr> [1..1]  54
     Name <Nm> [1..1] Text 54
     Value <Val> [1..1] Text 54
6.4.3.2.1  SystemSecuritiesAccount <SysSctiesAcct>
Presence: [1..1]
Definition: Account to or from which a securities entry is made.
SystemSecuritiesAccount <SysSctiesAcct> contains the following SystemSecuritiesAccount5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClosingDate <ClsgDt> [0..1] Date 52
   HoldIndicator <HldInd> [0..1] Indicator 52
   NegativePosition <NegPos> [0..1] Indicator 53
   EndInvestorFlag <EndInvstrFlg> [0..1] Text 53
   PricingScheme <PricgSchme> [0..1] Text 53
6.4.3.2.1.1  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Legal closing date of the securities account.
Datatype: "ISODate" on page 97
6.4.3.2.1.2  HoldIndicator <HldInd>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 52 December 2019
```

