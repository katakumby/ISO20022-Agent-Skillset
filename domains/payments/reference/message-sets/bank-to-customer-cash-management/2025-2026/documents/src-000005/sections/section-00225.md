---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.17 CardTransaction <CardTx>", "3.4.2.15.17.2 POI <POI>", "3.4.2.15.17.2.1 Identification <Id>"]
file_pages: [347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.17.2.1 Identification <Id>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 347 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
POI <POI> contains the following PointOfInteraction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 347
   SystemName <SysNm> [0..1] Text 348
   GroupIdentification <GrpId> [0..1] Text 348
   Capabilities <Cpblties> [0..1]  348
     CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 348
     CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 349
     OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 349
     DisplayCapabilities <DispCpblties> [0..*]  350
       DisplayType <DispTp> [1..1] CodeSet 350
       NumberOfLines <NbOfLines> [1..1] Text 350
       LineWidth <LineWidth> [1..1] Text 350
     PrintLineWidth <PrtLineWidth> [0..1] Text 350
   Component <Cmpnt> [0..*]  350
     POIComponentType <POICmpntTp> [1..1] CodeSet 351
     ManufacturerIdentification <ManfctrId> [0..1] Text 351
     Model <Mdl> [0..1] Text 351
     VersionNumber <VrsnNb> [0..1] Text 351
     SerialNumber <SrlNb> [0..1] Text 352
     ApprovalNumber <ApprvlNb> [0..*] Text 352
3.4.2.15.17.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the POI (Point Of Interaction) for the acquirer or its agent.
Identification <Id> contains the following elements (see "GenericIdentification32" on page 839 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 840
   Type <Tp> [0..1] CodeSet 840
   Issuer <Issr> [0..1] CodeSet 840
   ShortName <ShrtNm> [0..1] Text 841
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
347 March 2026
```

