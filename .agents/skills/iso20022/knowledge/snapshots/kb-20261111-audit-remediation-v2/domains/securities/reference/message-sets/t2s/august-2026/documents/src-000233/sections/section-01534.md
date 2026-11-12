---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "43.2 Structure"]
file_pages: [2156]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 43.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2156 to 2156.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2156

```text
43.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctModReq> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 2156
   AccountIdentification <AcctId> [1..1] ± 2157
   Modification <Mod> [1..*]  2157
     ScopeIndication <ScpIndctn> [1..1] CodeSet 2158
     RequestedModification <ReqdMod> [1..1]  2158
{Or       SystemSecuritiesAccount <SysSctiesAcct> [1..1]  2159
         ClosingDate <ClsgDt> [0..1] Date 2159
         HoldIndicator <HldInd> [0..1] Indicator 2159
         NegativePosition <NegPos> [0..1] Indicator 2160
         EndInvestorFlag <EndInvstrFlg> [0..1] Text 2160
         PricingScheme <PricgSchme> [0..1] Text 2160
Or       SystemRestriction <SysRstrctn> [1..1]  2160
         ValidFrom <VldFr> [1..1] DateTime 2160
         ValidTo <VldTo> [0..1] DateTime 2161
         Type <Tp> [1..1] Text 2161
Or}       MarketSpecificAttribute <MktSpcfcAttr> [1..1]  2161
         Name <Nm> [1..1] Text 2161
         Value <Val> [1..1] Text 2161
   SupplementaryData <SplmtryData> [0..*] ± C1 2161
43.3 Constraints
C1 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
43.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
43.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2156 August 2026
```

