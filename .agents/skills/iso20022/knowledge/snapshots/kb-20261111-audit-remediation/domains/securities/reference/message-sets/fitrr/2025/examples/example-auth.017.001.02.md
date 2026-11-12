---
template: false
document_kind: "source-example"
review_status: "needs-review"
domain: "securities"
source_ids: ["src-000320"]
source_editions: ["July 2025"]
message_sets: ["fitrr"]
message_ids: ["auth.017.001.02"]
literal_namespace: "urn:iso:std:iso:20022:tech:xsd:auth.017.001.01"
source_locations: [{"source_id": "src-000320", "heading_path": ["Business Examples", "Reference Data", "auth.017.001.02"], "heading_paragraph": "P256", "xml_first_paragraph": "P260", "xml_last_paragraph": "P357", "rendered_file_pages": [43, 44, 45]}]
issue_ids: ["issue-000055"]
limitations: ["Heading and literal namespace remain independent source claims. No example namespace, value or structure has been rewritten."]
---

# Source example — auth.017.001.02

[src-000320](../../../../../../../evidence/omitted/b0e9dc6419046e4d0523e995.md); heading P256; XML P260–P357; Word file pages 43–45.

**P257** Description

**P258** The following MessageInstance provides an example of a Reference Data message that is being reported by the Irish Stock Exchange.

**P259** Message Instance

## Literal source XML

```xml
<Document xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="urn:iso:std:iso:20022:tech:xsd:auth.017.001.01">
	<FinInstrmRptgRefDataRpt>
		<RptHdr>
			<RptgNtty>
				<MktIdCd>XDUB</MktIdCd>
			</RptgNtty>
			<RptgPrd>
				<Dt>2013-01-17</Dt>
			</RptgPrd>
			<SubmissnDtTm>2013-01-17T18:05:00</SubmissnDtTm>
		</RptHdr>
		<RefData>
			<TechRcrdId>2015-01-01000120</TechRcrdId>
			<FinInstrmGnlAttrbts>
				<Id>AB1234567890</Id>
				<FullNm>InstrumentFullNameHere</FullNm>
				<ShrtNm>HZL ČMB 4,45/10</ShrtNm>
				<ClssfctnTp>ESXXXX</ClssfctnTp>
				<NtnlCcy>EUR</NtnlCcy>
				<CmmdtyDerivInd>false</CmmdtyDerivInd>
			</FinInstrmGnlAttrbts>
			<Issr>EQYXK86SF381Q21S3020</Issr>
			<TradgVnRltdAttrbts>
				<Id>XDUB</Id>
				<IssrReq>false</IssrReq>
				<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>
			</TradgVnRltdAttrbts>
		</RefData>
		<RefData>
			<TechRcrdId>2015-01-01000121</TechRcrdId>
			<FinInstrmGnlAttrbts>
				<Id>AB1234567890</Id>
				<FullNm>InstrumentFullNameHere </FullNm>
				<ShrtNm>HZL ČMB 4,45/10</ShrtNm>
				<ClssfctnTp>DBVQFX</ClssfctnTp>
				<NtnlCcy>EUR</NtnlCcy>
				<CmmdtyDerivInd>false</CmmdtyDerivInd>
			</FinInstrmGnlAttrbts>
			<Issr>EQYXK86SF381Q21S3020</Issr>
			<TradgVnRltdAttrbts>
				<Id>XHEL</Id>
				<IssrReq>false</IssrReq>
				<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>
			</TradgVnRltdAttrbts>
			<DebtInstrmAttrbts>
				<TtlIssdNmnlAmt Ccy="CZK">349.60937</TtlIssdNmnlAmt>
				<MtrtyDt>2010-05-19</MtrtyDt>
				<NmnlValPerUnit Ccy="CZK">100.0</NmnlValPerUnit>
				<IntrstRate>
					<Fltg>
						<RefRate>
							<ISIN>PN5QWZKIH3L9</ISIN>
						</RefRate>
						<Term>
							<Unit>MNTH</Unit>
							<Val>232</Val>
						</Term>
						<BsisPtSprd>14300</BsisPtSprd>
					</Fltg>
				</IntrstRate>
				<DebtSnrty>JUND</DebtSnrty>
			</DebtInstrmAttrbts>
		</RefData>
		<RefData>
			<TechRcrdId>2015-01-01000122</TechRcrdId>
			<FinInstrmGnlAttrbts>
				<Id>AB1234567890</Id>
				<FullNm>InstrumentFullNameHere </FullNm>
				<ShrtNm>DAX9908TLOPENZ</ShrtNm>
				<ClssfctnTp>FFFPXX</ClssfctnTp>
				<NtnlCcy>EUR</NtnlCcy>
				<CmmdtyDerivInd>false</CmmdtyDerivInd>
			</FinInstrmGnlAttrbts>
			<Issr>885100KZRBC1KP0WDC71</Issr>
			<TradgVnRltdAttrbts>
				<Id>XLIS</Id>
				<IssrReq>false</IssrReq>
				<FrstTradDt>2015-02-23T00:00:00</FrstTradDt>
			</TradgVnRltdAttrbts>
			<DerivInstrmAttrbts>
				<XpryDt>2015-02-28</XpryDt>
				<PricMltplr>60.9</PricMltplr>
				<UndrlygInstrm>
					<Sngl>
						<ISIN>AJSQW9HOSNR8</ISIN>
					</Sngl>
				</UndrlygInstrm>
				<DlvryTp>PHYS</DlvryTp>
				<AsstClssSpcfcAttrbts>
					<FX>
						<FxTp>FXEM</FxTp>
						<OthrNtnlCcy>GHS</OthrNtnlCcy>
					</FX>
				</AsstClssSpcfcAttrbts>
			</DerivInstrmAttrbts>
		</RefData>
	</FinInstrmRptgRefDataRpt>
</Document>
```

## Checks and limitations

| Check | Result |
| --- | --- |
| XML well-formedness | pass |
| Heading definition | auth.017.001.02 |
| Literal namespace | urn:iso:std:iso:20022:tech:xsd:auth.017.001.01 |
| Heading/namespace agreement | fail |
| Exact literal-namespace schema validation | not-run |


[Canonical supplied definition named by heading](../../../../messages/auth.017.001.02/index.md) · [Detailed test evidence and errors](../../../../../../../tracking/reviews/fitrr-context-tables-examples.json)

The source example is preserved exactly. A valid XML document is not necessarily valid against the schema. A mismatched namespace is not silently updated to the heading version.
