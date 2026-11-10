---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "2.4 Message Building Blocks", "2.4.13 Signature <Sgntr>"]
file_pages: [17]
content_origin: "source-text-extraction"
mentioned_message_ids: ["head.001.001.02"]
---

# 2.4.13 Signature <Sgntr>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 17 to 17.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 17

```text
Constraints
• ValidationByTable
2.4.13 Signature <Sgntr>
Presence: [0..1]
Definition: Contains the digital signature of the Business Entity authorised to sign this Business
Message.
Type: (External Schema)
The W3C XML Schema that specifies following standard signature:
XML Signature Syntax and Processing (Second Edition) W3C Recommendation 10 June 2008
http://www.w3.org/TR/2008/REC-xmldsig-core-20080610/.
2.4.14 Related <Rltd>
Presence: [0..*]
Definition: Specifies the Business Application Header(s) of the Business Message(s) to which this
Business Message relates.
Can be used when replying to a query; can also be used when canceling or amending.
Related <Rltd> contains the following BusinessApplicationHeader5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CharacterSet <CharSet> [0..1] CodeSet C6 18
   From <Fr> [1..1]  18
{Or     OrganisationIdentification <OrgId> [1..1] ± 18
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 18
   To <To> [1..1]  19
{Or     OrganisationIdentification <OrgId> [1..1] ± 19
Or}     FinancialInstitutionIdentification <FIId> [1..1] ± 19
   BusinessMessageIdentifier <BizMsgIdr> [1..1] Text 20
   MessageDefinitionIdentifier <MsgDefIdr> [1..1] Text 20
   BusinessService <BizSvc> [0..1] Text 20
   CreationDate <CreDt> [1..1] DateTime 20
   CopyDuplicate <CpyDplct> [0..1] CodeSet 20
   PossibleDuplicate <PssblDplct> [0..1] Indicator 21
   Priority <Prty> [0..1] CodeSet C7 21
   Signature <Sgntr> [0..1] (External Schema) 22
Approved by the Securities SEG on 27 January 2026 head.001.001.02 BusinessApplicationHeaderV02
Corporate Actions - Maintenance 2025 - 2026 17 February 2026
```

