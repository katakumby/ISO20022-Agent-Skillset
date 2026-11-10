---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "43.4 Message Building Blocks", "43.4.3 Modification <Mod>", "43.4.3.1 ScopeIndication <ScpIndctn>"]
file_pages: [2158]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 43.4.3.1 ScopeIndication <ScpIndctn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2158 to 2158.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2158

```text
Modification <Mod> contains the following SecuritiesAccountModification2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ScopeIndication <ScpIndctn> [1..1] CodeSet 2158
   RequestedModification <ReqdMod> [1..1]  2158
{Or     SystemSecuritiesAccount <SysSctiesAcct> [1..1]  2159
       ClosingDate <ClsgDt> [0..1] Date 2159
       HoldIndicator <HldInd> [0..1] Indicator 2159
       NegativePosition <NegPos> [0..1] Indicator 2160
       EndInvestorFlag <EndInvstrFlg> [0..1] Text 2160
       PricingScheme <PricgSchme> [0..1] Text 2160
Or     SystemRestriction <SysRstrctn> [1..1]  2160
       ValidFrom <VldFr> [1..1] DateTime 2160
       ValidTo <VldTo> [0..1] DateTime 2161
       Type <Tp> [1..1] Text 2161
Or}     MarketSpecificAttribute <MktSpcfcAttr> [1..1]  2161
       Name <Nm> [1..1] Text 2161
       Value <Val> [1..1] Text 2161
43.4.3.1  ScopeIndication <ScpIndctn>
Presence: [1..1]
Definition: Specifies the type of requested modification.
Datatype: "DataModification1Code" on page 3235
CodeName Name Definition
INSE InsertNewDataSet Insert a new set of data.
UPDT UpdateDataSetDetails Update the details of an existing set of
data.
DELT DeleteDataSet Delete an existing set of data.
43.4.3.2  RequestedModification <ReqdMod>
Presence: [1..1]
Definition: Specifies which elements to be modified for the securities account reference data.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2158 August 2026
```

