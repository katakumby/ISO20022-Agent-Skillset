---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["58 reda.041.001.02 PartyActivityAdviceV02", "58.4 Message Building Blocks", "58.4.2 PartyActivity <PtyActvty>", "58.4.2.2 Change <Chng>", "58.4.2.2.2 Record <Rcrd>", "58.4.2.2.2.2 ContactDetails <CtctDtls>"]
file_pages: [2271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.041.001.02"]
---

# 58.4.2.2.2.2 ContactDetails <CtctDtls>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2271 to 2271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2271

```text
New <New> contains the following elements (see "PostalAddress28" on page 3093 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  3094
{Or     Code <Cd> [1..1] CodeSet 3094
Or}     Proprietary <Prtry> [1..1] ± 3095
   CareOf <CareOf> [0..1] Text 3095
   Department <Dept> [0..1] Text 3095
   SubDepartment <SubDept> [0..1] Text 3095
   StreetName <StrtNm> [0..1] Text 3095
   BuildingNumber <BldgNb> [0..1] Text 3096
   BuildingName <BldgNm> [0..1] Text 3096
   Floor <Flr> [0..1] Text 3096
   UnitNumber <UnitNb> [0..1] Text 3096
   PostBox <PstBx> [0..1] Text 3096
   Room <Room> [0..1] Text 3096
   PostCode <PstCd> [0..1] Text 3096
   TownName <TwnNm> [0..1] Text 3096
   TownLocationName <TwnLctnNm> [0..1] Text 3097
   DistrictName <DstrctNm> [0..1] Text 3097
   CountrySubDivision <CtrySubDvsn> [0..1] Text 3097
   Country <Ctry> [0..1] CodeSet C3 3097
   AddressLine <AdrLine> [0..7] Text 3097
   ValidFrom <VldFr> [0..1] Date 3097
58.4.2.2.2.2  ContactDetails <CtctDtls>
Presence: [1..1]
Definition: Specifies the contact details of the party.
ContactDetails <CtctDtls> contains the following UpdateLogContact2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Old <Od> [1..1] ± 2271
   New <New> [1..1] ± 2272
58.4.2.2.2.2.1  Old <Od>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.041.001.02 PartyActivityAdviceV02
Target2-Securities 2271 August 2026
```

