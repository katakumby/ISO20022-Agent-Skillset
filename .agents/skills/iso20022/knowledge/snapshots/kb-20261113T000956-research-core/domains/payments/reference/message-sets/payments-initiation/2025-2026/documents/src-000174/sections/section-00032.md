---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.7 ChequeInstruction <ChqInstr>", "2.4.2.19.7.3 ChequeFrom <ChqFr>", "2.4.2.19.7.3.2 Address <Adr>"]
file_pages: [58]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.7.3.2 Address <Adr>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 58 to 58.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 58

```text
2.4.2.19.7.3.2  Address <Adr>
Presence: [1..1]
Definition: Postal address of a party.
Address <Adr> contains the following elements (see "PostalAddress27" on page 575 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  575
{Or     Code <Cd> [1..1] CodeSet 576
Or}     Proprietary <Prtry> [1..1] ± 576
   CareOf <CareOf> [0..1] Text 576
   Department <Dept> [0..1] Text 576
   SubDepartment <SubDept> [0..1] Text 577
   StreetName <StrtNm> [0..1] Text 577
   BuildingNumber <BldgNb> [0..1] Text 577
   BuildingName <BldgNm> [0..1] Text 577
   Floor <Flr> [0..1] Text 577
   UnitNumber <UnitNb> [0..1] Text 577
   PostBox <PstBx> [0..1] Text 577
   Room <Room> [0..1] Text 577
   PostCode <PstCd> [0..1] Text 578
   TownName <TwnNm> [0..1] Text 578
   TownLocationName <TwnLctnNm> [0..1] Text 578
   DistrictName <DstrctNm> [0..1] Text 578
   CountrySubDivision <CtrySubDvsn> [0..1] Text 578
   Country <Ctry> [0..1] CodeSet C18 578
   AddressLine <AdrLine> [0..7] Text 578
2.4.2.19.7.4  DeliveryMethod <DlvryMtd>
Presence: [0..1]
Definition: Specifies the delivery method of the cheque by the debtor's agent.
DeliveryMethod <DlvryMtd> contains one of the following ChequeDeliveryMethod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 59
Or}   Proprietary <Prtry> [1..1] Text 59
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 58 March 2026
```

