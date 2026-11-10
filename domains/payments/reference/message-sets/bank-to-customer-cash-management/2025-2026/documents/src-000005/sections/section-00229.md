---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "3.4 Message Building Blocks", "3.4.2 Statement <Stmt>", "3.4.2.15 Entry <Ntry>", "3.4.2.15.17 CardTransaction <CardTx>", "3.4.2.15.17.2 POI <POI>", "3.4.2.15.17.2.5 Component <Cmpnt>", "3.4.2.15.17.2.5.1 POIComponentType <POICmpntTp>"]
file_pages: [351]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.053.001.14"]
---

# 3.4.2.15.17.2.5.1 POIComponentType <POICmpntTp>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 351 to 351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 351

```text
Component <Cmpnt> contains the following PointOfInteractionComponent1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   POIComponentType <POICmpntTp> [1..1] CodeSet 351
   ManufacturerIdentification <ManfctrId> [0..1] Text 351
   Model <Mdl> [0..1] Text 351
   VersionNumber <VrsnNb> [0..1] Text 351
   SerialNumber <SrlNb> [0..1] Text 352
   ApprovalNumber <ApprvlNb> [0..*] Text 352
3.4.2.15.17.2.5.1  POIComponentType <POICmpntTp>
Presence: [1..1]
Definition: Type of component belonging to a POI Terminal.
Datatype: "POIComponentType1Code" on page 902
CodeName Name Definition
SOFT Soft Payment or other software application.
EMVK EMVKernel EMV application kernel (EMV is the chip
card specifications initially defined by
Eurocard, Mastercard and Visa).
EMVO EMVLevel1 EMV physical interface (EMV is the chip
card specifications initially defined by
Eurocard, Mastercard and Visa).
MRIT MerchantInterface Merchant interface.
CHIT CardholderInterface Cardholder Interface.
SECM SecureModule Security module.
PEDV PINEntryDevice Personal identification number (or PIN)
entry device (PED).
3.4.2.15.17.2.5.2  ManufacturerIdentification <ManfctrId>
Presence: [0..1]
Definition: Identification of the software, hardware or system provider of the POI component.
Datatype: "Max35Text" on page 916
3.4.2.15.17.2.5.3  Model <Mdl>
Presence: [0..1]
Definition: Identification of a model of POI component for a given manufacturer.
Datatype: "Max35Text" on page 916
3.4.2.15.17.2.5.4  VersionNumber <VrsnNb>
Presence: [0..1]
Definition: Version of component belonging to a given model.
Approved by the Payments SEG on 12 January 2026 camt.053.001.14 BankToCustomerStatementV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
351 March 2026
```

