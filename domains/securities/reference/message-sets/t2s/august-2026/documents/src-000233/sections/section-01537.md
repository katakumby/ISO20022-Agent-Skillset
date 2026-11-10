---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["43 reda.023.001.01 SecuritiesAccountModificationRequestV01", "43.4 Message Building Blocks", "43.4.3 Modification <Mod>", "43.4.3.2 RequestedModification <ReqdMod>", "43.4.3.2.1 SystemSecuritiesAccount <SysSctiesAcct>"]
file_pages: [2159]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.023.001.01"]
---

# 43.4.3.2.1 SystemSecuritiesAccount <SysSctiesAcct>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2159 to 2159.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2159

```text
RequestedModification <ReqdMod> contains one of the following
SecuritiesAccountModification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SystemSecuritiesAccount <SysSctiesAcct> [1..1]  2159
     ClosingDate <ClsgDt> [0..1] Date 2159
     HoldIndicator <HldInd> [0..1] Indicator 2159
     NegativePosition <NegPos> [0..1] Indicator 2160
     EndInvestorFlag <EndInvstrFlg> [0..1] Text 2160
     PricingScheme <PricgSchme> [0..1] Text 2160
Or   SystemRestriction <SysRstrctn> [1..1]  2160
     ValidFrom <VldFr> [1..1] DateTime 2160
     ValidTo <VldTo> [0..1] DateTime 2161
     Type <Tp> [1..1] Text 2161
Or}   MarketSpecificAttribute <MktSpcfcAttr> [1..1]  2161
     Name <Nm> [1..1] Text 2161
     Value <Val> [1..1] Text 2161
43.4.3.2.1  SystemSecuritiesAccount <SysSctiesAcct>
Presence: [1..1]
Definition: Account to or from which a securities entry is made.
SystemSecuritiesAccount <SysSctiesAcct> contains the following SystemSecuritiesAccount5
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClosingDate <ClsgDt> [0..1] Date 2159
   HoldIndicator <HldInd> [0..1] Indicator 2159
   NegativePosition <NegPos> [0..1] Indicator 2160
   EndInvestorFlag <EndInvstrFlg> [0..1] Text 2160
   PricingScheme <PricgSchme> [0..1] Text 2160
43.4.3.2.1.1  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Legal closing date of the securities account.
Datatype: "ISODate" on page 3319
43.4.3.2.1.2  HoldIndicator <HldInd>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.023.001.01
SecuritiesAccountModificationRequestV01
Target2-Securities 2159 August 2026
```

