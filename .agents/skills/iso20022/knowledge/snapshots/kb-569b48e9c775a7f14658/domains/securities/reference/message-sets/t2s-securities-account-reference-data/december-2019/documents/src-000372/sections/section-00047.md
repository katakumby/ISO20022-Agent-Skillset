---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["6 reda.023.001.01 SecuritiesAccountModificationRequestV01", "6.4 Message Building Blocks", "6.4.3 Modification <Mod>", "6.4.3.1 ScopeIndication <ScpIndctn>"]
file_pages: [51]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 6.4.3.1 ScopeIndication <ScpIndctn>

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 51 to 51.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 51

```text
Modification <Mod> contains the following SecuritiesAccountModification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ScopeIndication <ScpIndctn> [1..1] CodeSet 51
   RequestedModification <ReqdMod> [1..1]  51
{Or     SystemSecuritiesAccount <SysSctiesAcct> [1..1]  52
       ClosingDate <ClsgDt> [0..1] Date 52
       HoldIndicator <HldInd> [0..1] Indicator 52
       NegativePosition <NegPos> [0..1] Indicator 53
       EndInvestorFlag <EndInvstrFlg> [0..1] Text 53
       PricingScheme <PricgSchme> [0..1] Text 53
Or     SystemRestriction <SysRstrctn> [1..1]  53
       ValidFrom <VldFr> [1..1] DateTime 53
       ValidTo <VldTo> [0..1] DateTime 54
       Type <Tp> [1..1] Text 54
Or}     MarketSpecificAttribute <MktSpcfcAttr> [1..1]  54
       Name <Nm> [1..1] Text 54
       Value <Val> [1..1] Text 54
6.4.3.1  ScopeIndication <ScpIndctn>
Presence: [1..1]
Definition: Specifies the type of requested modification.
Datatype: "DataModification1Code" on page 94
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
6.4.3.2  RequestedModification <ReqdMod>
Presence: [1..1]
Definition: Specifies which elements to be modified for the securities account reference data.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities - Securities Account Reference Data 51 December 2019
```

