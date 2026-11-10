---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["1 Message Set Overview", "2.4 Message Building Blocks", "2.4.2 Report <Rpt>", "2.4.2.15 Entry <Ntry>", "2.4.2.15.18 EntryDetails <NtryDtls>", "2.4.2.15.18.2 TransactionDetails <TxDtls>", "2.4.2.15.18.2.26 CardTransaction <CardTx>", "2.4.2.15.18.2.26.2 POI <POI>", "2.4.2.15.18.2.26.2.1 Identification <Id>"]
file_pages: [241]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.052.001.14"]
---

# 2.4.2.15.18.2.26.2.1 Identification <Id>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 241 to 241.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 241

```text
POI <POI> contains the following PointOfInteraction1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 241
   SystemName <SysNm> [0..1] Text 242
   GroupIdentification <GrpId> [0..1] Text 242
   Capabilities <Cpblties> [0..1]  242
     CardReadingCapabilities <CardRdngCpblties> [0..*] CodeSet 242
     CardholderVerificationCapabilities
<CrdhldrVrfctnCpblties>
[0..*] CodeSet 243
     OnLineCapabilities <OnLineCpblties> [0..1] CodeSet 243
     DisplayCapabilities <DispCpblties> [0..*]  244
       DisplayType <DispTp> [1..1] CodeSet 244
       NumberOfLines <NbOfLines> [1..1] Text 244
       LineWidth <LineWidth> [1..1] Text 244
     PrintLineWidth <PrtLineWidth> [0..1] Text 244
   Component <Cmpnt> [0..*]  244
     POIComponentType <POICmpntTp> [1..1] CodeSet 245
     ManufacturerIdentification <ManfctrId> [0..1] Text 245
     Model <Mdl> [0..1] Text 245
     VersionNumber <VrsnNb> [0..1] Text 245
     SerialNumber <SrlNb> [0..1] Text 246
     ApprovalNumber <ApprvlNb> [0..*] Text 246
2.4.2.15.18.2.26.2.1  Identification <Id>
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
Approved by the Payments SEG on 12 January 2026 camt.052.001.14
BankToCustomerAccountReportV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
241 March 2026
```

