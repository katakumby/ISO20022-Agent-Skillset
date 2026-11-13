---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 camt.053.001.14 BankToCustomerStatementV14", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.2.14 Entry <Ntry>", "4.4.2.14.18 EntryDetails <NtryDtls>", "4.4.2.14.18.2 TransactionDetails <TxDtls>", "4.4.2.14.18.2.26 CardTransaction <CardTx>", "4.4.2.14.18.2.26.2 POI <POI>", "4.4.2.14.18.2.26.2.5 Component <Cmpnt>", "4.4.2.14.18.2.26.2.5.1 POIComponentType <POICmpntTp>"]
file_pages: [763]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.054.001.14"]
---

# 4.4.2.14.18.2.26.2.5.1 POIComponentType <POICmpntTp>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 763 to 763.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 763

```text
Component <Cmpnt> contains the following PointOfInteractionComponent1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   POIComponentType <POICmpntTp> [1..1] CodeSet 763
   ManufacturerIdentification <ManfctrId> [0..1] Text 763
   Model <Mdl> [0..1] Text 763
   VersionNumber <VrsnNb> [0..1] Text 763
   SerialNumber <SrlNb> [0..1] Text 764
   ApprovalNumber <ApprvlNb> [0..*] Text 764
4.4.2.14.18.2.26.2.5.1  POIComponentType <POICmpntTp>
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
4.4.2.14.18.2.26.2.5.2  ManufacturerIdentification <ManfctrId>
Presence: [0..1]
Definition: Identification of the software, hardware or system provider of the POI component.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.2.5.3  Model <Mdl>
Presence: [0..1]
Definition: Identification of a model of POI component for a given manufacturer.
Datatype: "Max35Text" on page 916
4.4.2.14.18.2.26.2.5.4  VersionNumber <VrsnNb>
Presence: [0..1]
Definition: Version of component belonging to a given model.
Approved by the Payments SEG on 12 January 2026 camt.054.001.14
BankToCustomerDebitCreditNotificationV14
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
763 March 2026
```

