---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.17 CardTransaction <CardTx>", "4.4.2.14.17.2 POI <POI>", "4.4.2.14.17.2.1 Identification <Id>"]
file_pages: [605]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.17.2.1 Identification <Id>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 605 to 605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 605

```text
POI <POI> contains the following PointOfInteraction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 605
   SystemName <SysNm> [0..1] Text 606
   GroupIdentification <GrpId> [0..1] Text 606
   Capabilities <Cpblties> [0..1]  606
     CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 606
     CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 607
     OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 607
     DisplayCapabilities <DispCpblties> [0..*]  608
       DisplayType <DispTp> [1..1] CodeSet 608
       NumberOfLines <NbOfLines> [1..1] Text 608
       LineWidth <LineWidth> [1..1] Text 608
     PrintLineWidth <PrtLineWidth> [0..1] Text 608
   Component <Cmpnt> [0..*]  608
     POIComponentType <POICmpntTp> [1..1] CodeSet 609
     ManufacturerIdentification <ManfctrId> [0..1] Text 609
     Model <Mdl> [0..1] Text 609
     VersionNumber <VrsnNb> [0..1] Text 609
     SerialNumber <SrlNb> [0..1] Text 610
     ApprovalNumber <ApprvlNb> [0..*] Text 610
4.4.2.14.17.2.1  Identification <Id>
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
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
605 March 2026
```

