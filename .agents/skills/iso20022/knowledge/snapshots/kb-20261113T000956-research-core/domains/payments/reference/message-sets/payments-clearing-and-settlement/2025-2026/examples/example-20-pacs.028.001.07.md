---
template: false
document_kind: "message-example"
title: "FIToFIPaymentStatusRequest - pacs.028.001.07"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000172"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.028.001.07"]
message_families: ["pacs.028"]
source_locations: [{"source_id": "src-000162", "locator": "P2514–P2615; T47", "heading_path": ["Business Examples", "FIToFIPaymentStatusRequest - pacs.028.001.07"]}, {"source_id": "src-000172", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-def-electronics-bf4c618"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FIToFIPaymentStatusRequest - pacs.028.001.07

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P2506** FIToFIPaymentStatusRequest - pacs.028.001.07

**P2507** Description

**P2508** This example relates to the instruction message in section 7.6.1, a FIToFICustomerCreditTransfer message sent by BBBBUS33 to AAAAGB2L. No FIToFIPaymentStatusReport message was received yet, but BBBBUS33 wants to know the status of the instruction. BBBBUS33 therefore sends a FIToFIPaymentStatusRequest message to request a FIToFIPaymentStatusReport.

**P2509** Business Data

**P2510** The FIToFIPaymentStatusRequest message, from Bank BBBBUS33 to Bank AAAAGB2L:

**P2513** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0047.md) · [Literal XML payload](../../../../../../../evidence/archived/5b4de48084835d70aae7d375.md) · [Source example flow](../flows/example-src-000162-20.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | InstgAgt | /FIToFIPmtStsReq/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | InstdAgt | /FIToFIPmtStsReq/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr | /FIToFIPmtStsReq/TxInf/OrgnlTxRef/Dbtr/Pty/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FIToFIPmtStsReq/TxInf/OrgnlTxRef/DbtrAgt/FinInstnId/BICFI |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | CdtrAgt | /FIToFIPmtStsReq/TxInf/OrgnlTxRef/CdtrAgt/FinInstnId/BICFI |
| [DEF Electronics](../../../../../../../shared/reference/participants/participant-src-000162-example-def-electronics-bf4c618.md) | Cdtr | /FIToFIPmtStsReq/TxInf/OrgnlTxRef/Cdtr/Pty/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.028.001.07 and wrapped in Document passed the exact supplied XSD src-000172. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFIPmtStsReq>
	<GrpHdr>
		<MsgId>BBBB/150929-CCT/JPY/456</MsgId>
		<CreDtTm>2015-09-28T16:06:00</CreDtTm>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<OrgnlGrpInf>
		<OrgnlMsgId>BBBB/150928-CCT/JPY/123</OrgnlMsgId>
		<OrgnlMsgNmId>pacs.008.001.12 </OrgnlMsgNmId>
		<OrgnlCreDtTm>2015-09-28T16:00:00</OrgnlCreDtTm>
	</OrgnlGrpInf>
	<TxInf>
		<StsReqId>BBBB/150928-CCT/JPY/456Request</StsReqId>
		<OrgnlInstrId>BBBB/150928-CCT/JPY/123/1</OrgnlInstrId>
		<OrgnlEndToEndId>ABC/4562/2015-09-08</OrgnlEndToEndId>
		<OrgnlTxId>BBBB/150928-CCT/JPY/123/1</OrgnlTxId>
		<AccptncDtTm>2015-09-28T15:45:00</AccptncDtTm>
		<OrgnlTxRef>
			<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
			<IntrBkSttlmDt>2015-09-28</IntrBkSttlmDt>
			<PmtTpInf>
				<InstrPrty>NORM</InstrPrty>
			</PmtTpInf>
			<RmtInf>
				<Strd>
					<RfrdDocInf>
						<Tp>
							<CdOrPrtry>
								<Cd>CINV</Cd>
							</CdOrPrtry>
						</Tp>
						<Nb>4562</Nb>
						<RltdDt>
						<Tp>
							<Cd>INDA</Cd>
						</Tp>
						<Dt>2015-09-08</Dt>									
						</RltdDt>							
					</RfrdDocInf>
				</Strd>
			</RmtInf>
			<Dbtr>
				<Pty>
					<Nm>ABC Corporation</Nm>
					<PstlAdr>
						<StrtNm>Times Square</StrtNm>
						<BldgNb>7</BldgNb>
						<PstCd>NY 10036</PstCd>
						<TwnNm>New York</TwnNm>
						<Ctry>US</Ctry>
					</PstlAdr>
				</Pty>
			</Dbtr>
			<DbtrAcct>
				<Id>
					<Othr>
						<Id>00125574999</Id>
					</Othr>
				</Id>
			</DbtrAcct>
			<DbtrAgt>
				<FinInstnId>
					<BICFI>BBBBUS33</BICFI>
				</FinInstnId>
			</DbtrAgt>
			<CdtrAgt>
				<FinInstnId>
					<BICFI>AAAAGB2L</BICFI>
				</FinInstnId>
			</CdtrAgt>
			<Cdtr>
				<Pty>
					<Nm>DEF Electronics</Nm>
					<PstlAdr>
						<StrtNm>Mark Lane</StrtNm>
						<BldgNb>55</BldgNb>
						<PstCd>EC3R7NE</PstCd>
						<TwnNm>London</TwnNm>
						<Ctry>GB</Ctry>
						<AdrLine>Corn Exchange 5th Floor</AdrLine>
					</PstlAdr>
				</Pty>
			</Cdtr>
			<CdtrAcct>
				<Id>
					<Othr>
						<Id>23683707994215</Id>
					</Othr>
				</Id>
			</CdtrAcct>
		</OrgnlTxRef>
	</TxInf>
</FIToFIPmtStsReq>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-20.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
