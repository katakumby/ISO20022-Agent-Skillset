---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.2 Warrant <Warrt>", "28.4.2.1.3.1.2.3 Type <Tp>", "28.4.2.1.3.1.2.3.1 Code <Cd>"]
file_pages: [1405]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.2.3.1 Code <Cd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1405 to 1405.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1405

```text
Definition: Indicates when a warrant can be exercised.
Type <Tp> contains one of the following WarrantStyle3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1405
Or}   Proprietary <Prtry> [1..1] ± 1405
28.4.2.1.3.1.2.3.1  Code <Cd>
Presence: [1..1]
Definition: Warrant style expressed as an ISO 20022 code.
Datatype: "WarrantStyle1Code" on page 3319
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
28.4.2.1.3.1.2.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Warrant style expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
28.4.2.1.3.1.2.4  WarrantAgent <WarrtAgt>
Presence: [0..*]
Definition: Entity appointed by the issuer to process the exercising of warrants, sometimes responsible
for the issuance of the warrants into the market.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1405 August 2026
```

