---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "6.2 Structure"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 6.2 Structure

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctModReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 49
   AccountIdentification <AcctId> [1..1] ± 50
   Modification <Mod> [1..*]  50
     ScopeIndication <ScpIndctn> [1..1] CodeSet 51
     RequestedModification <ReqdMod> [1..1]  51
{Or       SystemSecuritiesAccount <SysSctiesAcct> [1..1]  52
         ClosingDate <ClsgDt> [0..1] Date 52
         HoldIndicator <HldInd> [0..1] Indicator 52
         NegativePosition <NegPos> [0..1] Indicator 53
         EndInvestorFlag <EndInvstrFlg> [0..1] Text 53
         PricingScheme <PricgSchme> [0..1] Text 53
Or       SystemRestriction <SysRstrctn> [1..1]  53
         ValidFrom <VldFr> [1..1] DateTime 53
         ValidTo <VldTo> [0..1] DateTime 54
         Type <Tp> [1..1] Text 54
Or}       MarketSpecificAttribute <MktSpcfcAttr> [1..1]  54
         Name <Nm> [1..1] Text 54
         Value <Val> [1..1] Text 54
   SupplementaryData <SplmtryData> [0..*] ± C1 54
6.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 49 December 2019
```

